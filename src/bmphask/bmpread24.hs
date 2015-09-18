module Main where

{-
24bitbmp用
40bitinfo
windows bitmap
-}

import System.Environment(getArgs)
import qualified Data.ByteString.Lazy as Bl
import Numeric (showHex)

cfold = foldr (++) []

rsInt :: (Show a,Read a)=> a -> Int
rsInt = read . show

dropTake :: Int -> Int -> [a] -> [a]
dropTake d t = (take t) . (drop d)
dropTakeSame dt = dropTake dt dt

tbgr 0 _  = []
tbgr _ [] = []
tbgr n xs = (take 3 xs) : tbgr (n-1) (drop 3 xs)

plusp a [[]] = a
plusp a b = a ++ b

takeBGR _ [] = []
takeBGR n xs = ( lineData `plusp` [bs] ) : takeBGR n next
  where 
    lineData = (tbgr n xs)
    ml4 = mod (length lineData) 4
    ds = drop (n*3) xs
    bs = take ml4 ds
    next = drop ml4 ds

-- (read . show) $ div (rsInt b) 2

bgr2Red (b:g:r:[]) = [0,0,r]
  --if and [(rsInt r) >= 128 , (rsInt b) < 100 , (rsInt g) < 100]
  --                      then [b,g,r]
  --                      else [0,0,0]
bgr2Red as = as

main = do
  a <- getArgs
  f <- Bl.readFile $ head a
  let file = Bl.unpack f
  let fileHeader = dropTake 0 14 file
  let infoHeader = dropTake 14 40 file
  --let color = dropTake 54 0 file
  let imgData = drop 54 file

  --print fileHeader
  --print infoHeader

  let xsize = rsInt (head $ dropTake 4 4 infoHeader)

  --let xsize = 4

  --print $ takeBGR xsize imgData

  --let readData = Bl.pack $ fileHeader ++ infoHeader ++ imgData

  let readData = Bl.pack $ fileHeader ++ infoHeader ++ (cfold $ map cfold $ (map (map bgr2Red) ) $ takeBGR xsize imgData) 

  Bl.writeFile (( (init . init . init . init) (head a) )++ "read.bmp") readData
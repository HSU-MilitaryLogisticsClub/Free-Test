module Main where

import qualified Data.ByteString.Lazy as Bl

xsize = 12
ysize = 12

rs = read . show
cfold = foldr (++) []

fileHead = cfold [[66,77],[rs (length file), 00 , 00 , 00],[00,00],[00,00],[rs ((length fileHead)+(length infoHeader)+(length colorPallet)),00,00,00]]

infoHeader = cfold [[40,00,00,00],[xsize,00,00,00],[ysize,00,00,00],[01,00],[01,00],[00,00,00,00],[rs (length imgData),00,00,00],[00,00,00,00],[00,00,00,00],[00,00,00,00],[00,00,00,00]]

colorPallet = cfold [[00,00,00,00],[255,255,255,00]]

imgData = cfold [[00,00,00,00],[00,00,00,00],[00,00,00,00],[00,00,00,00],[00,00,00,00],[00,00,00,00],[00,00,00,00],[00,00,00,00],[00,00,00,00],[00,00,00,00],[00,00,00,00],[00,00,00,00]]

file = fileHead ++ infoHeader ++ colorPallet ++ imgData

main = do
  print $ Bl.pack file
  Bl.writeFile "a.bmp" $ Bl.pack file
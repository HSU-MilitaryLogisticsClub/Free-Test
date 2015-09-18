#coding: utf-8

def hex2bin str
  if (str == "a")
    return 10
  elsif (str == "b")
    return 11
  elsif (str == "c")
    return 12
  elsif (str == "d")
    return 13
  elsif (str == "e")
    return 14
  elsif (str == "f")
    return 15
  else
    return str.to_i
  end
end

def h2b sbin
  return ((hex2bin sbin[2]) *16) + (hex2bin sbin[3])
end

a = `sudo i2cset -y 1 0x6a 0x20 0x0f i`

val_l = `sudo i2cget -y 1 0x6a 0x28`
val_h = `sudo i2cget -y 1 0x6a 0x29`

x = (h2b val_h * 256) + (h2b val_l)
puts x
# puts (x *  0.00875)
# puts (x * 0.0175)
puts (x * 0.07)
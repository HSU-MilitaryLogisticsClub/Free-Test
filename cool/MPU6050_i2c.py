import commands
import math


def i2cGetWord(addr):
	out = commands.getoutput("sudo i2cget -y 1 0x68 "+ addr + " w")
	return (out[4]+out[5]+out[2]+out[3])

def i2cGetWord_HMC5883L(addr):
	out = commands.getoutput("sudo i2cget -y 1 0x1e "+ addr + " w")
	return (out[4]+out[5]+out[2]+out[3])


#MPU6050
def accel_X():
	return i2cGetWord("0x3B")

def accel_Y():
	return i2cGetWord("0x3D")

def accel_Z():
	return i2cGetWord("0x3F")

def gyro_roll():
	return i2cGetWord("0x43")

def gyro_pitch():
	return i2cGetWord("0x45")

def gyro_yaw():
	return i2cGetWord("0x47")

def trans_accel(a):
	return ((a / 2048.0)*9.80665)

def trans_gyro(g):
	return (g / 16.4)

def dist(a,b):
    return math.sqrt((a*a)+(b*b))

#def get_y_rotation(x,y,z):
    #radians = math.atan2(x, dist(y,z))
    #return -math.degrees(radians)

#def get_x_rotation(x,y,z):
    #radians = math.atan2(y, dist(x,z))
    #return math.degrees(radians)


#HMC5883
def mag_x():
	return i2cGetWord_HMC5883L("0x03")

def mag_y():
	return i2cGetWord_HMC5883L("0x07")

def mag_z():
	return i2cGetWord_HMC5883L("0x05")

def trans_magx(mgx):
	return mgx*0.92

def trans_magy(mgy):
	return mgy*0.92

def trans_magz(mgz):
	return mgz*0.92


def vectorH(mgx,mgy):
	vec_H = (mgx**2)+(mgy**2)
	math.sqrt(vec_H)
	return vec_H

def vectorR(mgx,mgy,mgz):
	vec_R = (mgx,mgy,mgz)
	math.sqrt(vec_R)
	return vec_R


def trans_magneticvecterD(mgy,mgx):
	radiansD = math.atan2(mgy,mgx)
	return math.degrees(radiansD)

def trans_magneticvecterI(mgz,vec_H):
	radiansI = math.atan2(mgz,vec_H)
	return math.degrees(radiansI)



def vector(radiansD):
	deg = 90.0-radiansD
	return deg



def Hex2Dec(str0):
    su = 0
    for x in range(0,len(str0)):
        if '0' <= str0[x] and str0[x] <= '9':
            n = int(str0[x])
        elif 'a' <= str0[x] and str0[x] <= 'f':
            n = ord(str0[x]) - ord('a') + 10
        else :
            return "baka"
        su = su * 16 + n
    return su

def sing(m):
	if 32768 <= m:
		return(m - 65536)
	elif 32768 > m:
		return(m)
	else :
		return("continue")


def __init__():

	#MPU6050
	#commands.getoutput("sudo i2cset -y 1 0x68 0x6B 0x00")
	#commands.getoutput("sudo i2cset -y 1 0x68 0x6C 0x00")
	#print "initialize_ok"

	#commands.getoutput("sudo i2cset -y 1 0x68 0x1B 0x18")
	#commands.getoutput("sudo i2cset -y 1 0x68 0x1C 0x18")
	#print "scale 16[G]_2500[deg/sec]"
	
	#HMC5883L
	commands.getoutput("sudo i2cset -y 1 0x1e 0x02 0x00")
	commands.getoutput("sudo i2cset -y 1 0x1e 0x09")
	commands.getoutput("sudo i2cset -y 1 0x1e 0x20 0x40") #0.92 [mG/LSB]
	#print "X [m/sec^2],Y [m/sec^2],Z [m/sec^2],roll [deg/sec],pitch [deg/sec],yaw [deg/sec],x_revolution [deg],y_revolution [deg]"




if __name__ == '__main__':
	__init__()
	for x in range(0,10):
		#print x
		#print "X_axics,",trans_accel(sing(Hex2Dec(accel_X()))), ",[m/sec^2]"
		#print "Y_axics,",trans_accel(sing(Hex2Dec(accel_Y()))), ",[m/sec^2]"
		#print "Z_axics,",trans_accel(sing(Hex2Dec(accel_Z()))), ",[m/sec^2]"
		#print "Roll,",trans_gyro(sing(Hex2Dec(gyro_roll()))), ",[deg/sec]"
		#print "Pitch,",trans_gyro(sing(Hex2Dec(gyro_pitch()))), ",[deg/sec]"
		#print "Yaw,",trans_gyro(sing(Hex2Dec(gyro_yaw()))), ",[deg/sec]"

		#print trans_accel(sing(Hex2Dec(accel_X()))),",",trans_accel(sing(Hex2Dec(accel_Y()))),",",trans_accel(sing(Hex2Dec(accel_Z()))),",",trans_gyro(sing(Hex2Dec(gyro_roll()))),",",trans_gyro(sing(Hex2Dec(gyro_pitch()))),",",trans_gyro(sing(Hex2Dec(gyro_yaw()))),",",get_x_rotation(trans_accel(sing(Hex2Dec(accel_X()))),trans_accel(sing(Hex2Dec(accel_Y()))),trans_accel(sing(Hex2Dec(accel_Z())))),",",get_y_rotation(trans_accel(sing(Hex2Dec(accel_X()))),trans_accel(sing(Hex2Dec(accel_Y()))),trans_accel(sing(Hex2Dec(accel_Z()))))

		#print  sing(Hex2Dec(mag_x())),",",sing(Hex2Dec(mag_y())),",",sing(Hex2Dec(mag_z()))

		print trans_magx(sing(Hex2Dec(mag_x()))),",",trans_magy(sing(Hex2Dec(mag_y()))),",",trans_magneticvecterD(trans_magy(sing(Hex2Dec(mag_y()))),trans_magx(sing(Hex2Dec(mag_x())))),",",vector(trans_magneticvecterD(trans_magy(sing(Hex2Dec(mag_y()))),trans_magx(sing(Hex2Dec(mag_x())))))










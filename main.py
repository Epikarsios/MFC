from MFC import MFC
import serial

flow =MFC()

myval = raw_input('Enter SetPoint ')


val = flow.SetPoint_Write(myval)


s = serial.Serial('/dev/ttyUSB0')

s.write(val)
#a =s.read(12)

#print 'First read  '
#print a

myu = raw_input('Enter units 1-30 ')

slm = flow.Units_Write(myu)
s.write(slm)

mode = 'On'

#print 'Attempt Echo mode'
#strmode =flow.Stream_Write(mode)



#s.write(strmode)
newval = raw_input('Enter SetPoint')
nnval = flow.SetPoint_Write(newval)
s.write(nnval)
#b = s.read(12)
#print 'Second read'

#print b

#qw = flow.SetPoint_Read()
#s.write(qw)
#ree = s.read(12)
#print ree

s.close()

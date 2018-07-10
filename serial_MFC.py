import serial
import io



s = serial.Serial('/dev/ttyUSB0')   # Open Serial Port
print(s.name)
msg_Rx =s.read(10)
print( msg_Rx)

myarray = [33, 83, 101, 116, 102, 48, 46, 48, 49, 49, 136, 195, 13]

stopf = [33,83,101,116,102,48,46,48,48, 48,171,211,13]
mycode = '21 53 65 74 66 30 2e 30 31 31 88 c3 0d'



# This Works
s.write(myarray)
msg_Rx2 =s.read(10)


#   This Works!!!
#s.write([33, 83, 101, 116, 102, 48, 46, 48, 49, 49, 136, 195, 13])




print  ("Sending  ")

print(msg_Rx2)

s.close()
print('Closed')

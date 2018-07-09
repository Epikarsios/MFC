from MFC import MFC
import serial
flow = MFC()

msg = input("Enter Value ")

cmd = flow.SetPoint_Write(msg)
print(cmd)

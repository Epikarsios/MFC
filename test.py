import ChkUsrInputX
from MFC import MFC
mfc = MFC()



msg = input("Enter Numerical Value ")


if ChkUsrInputX.chkUsrNum(msg):
	print("it worked! was True")
	cmd = mfc.SetPoint_Write(msg)
	print(cmd)
else: 
	print ("it was false")




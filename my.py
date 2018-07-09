from MFC import MFC

flow = MFC()

msg = input("Enter Value ")

cmd = flow.SetPoint_Write(msg)
print(cmd)

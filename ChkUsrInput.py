from sets import Set



def chkUsrNum(str_Cmd):
	allowed_Chars = Set('0123456789.')
	if Set(str_Cmd).issubset(allowed_Chars) and str_Cmd:
		numDecPoint = str_Cmd.count('.')
		if numDecPoint > 1:
			print("Too many decimal ps.")
			return False
		else:
			print("Valid number")
			return True
	else:
		print("Not a valid number")
		return False


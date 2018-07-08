



def chkUsrNum(str_Cmd):
	
	allowed_Chars = set('0123456789.')
	if set(str_Cmd).issubset(allowed_Chars) and str_Cmd:
		numDecPoint = str_Cmd.count('.')
		if numDecPoint > 1:
			print('Too many decimal points.')
			return False
		else:
			if float(str_Cmd)> 0.0009 and float(str_Cmd)< 10:
				print( 'Valid number')
				return True
			else:
				print( 'Out Of Range')
	else:
		print( 'Not a valid number')
		return False


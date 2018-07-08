import crcmod.predefined
import binascii


crc_func = crcmod.predefined.mkCrcFun('crc-ccitt-false')

def str2_dec_array(str):
	hex_str = binascii.b2a_hex(str)


	hex_crc_temp = hex(crc_func(str))
	hex_crc = hex_crc_temp[2:]


	dec_array = []
	Term = 13
	for i in hex_str.decode("hex"):
		dec_array.append(ord(i))

	for j in hex_crc.decode("hex"):
		dec_array.append(ord(j))


	dec_array.append(Term)
	return dec_array

class MFC:

	def SetPoint_Read(self):
		str_Cmd ='?Setf'
		dec_array = str2_dec_array(str_Cmd)
		return dec_array

	def SetPoint_Write(self,Value):
		str_Cmd = '!Setf'+Value  #Creates str from Cmd and Val 
		dec_array = str2_dec_array(str_Cmd) #str+crc+cr array 
		return dec_array

	def Flow_Read(self):
		str_Cmd = '?Flow'
		dec_array = str2_dec_array(str_Cmd)
		return dec_array

	def Units_Read(self):
		str_Cmd = '?Unti'
		dec_array = str2_dec_array(str_Cmd)
		return dec_array

	def Units_Write(self,Value):
		str_Cmd = '!Unti'+ Value
		dec_array = str2_dec_array(str_Cmd)
		return dec_array

	def ValveState_Read(self):
		str_Cmd = '?Vlvi'
		dec_array = str2_dec_array(str_Cmd)
		return dec_array

	def ValveState_Write(self,Value):
		str_Cmd = '!Vlvi'+ Value
		dec_array = str2_dec_array(str_Cmd)
		return dec_array

	def Stream_Read(self):
		str_Cmd = '?Strm'
		dec_array = str2_dec_array(str_Cmd)
		return dec_array

	def Stream_Write(self, Value):
		str_Cmd = '!Strm'+ Value
		dec_array = str2_dec_array(str_Cmd)
		return dec_array

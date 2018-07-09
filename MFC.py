import crcmod.predefined
import binascii


crc_func = crcmod.predefined.mkCrcFun('crc-ccitt-false')

def str2_dec_array(str):
	bin_str = binascii.a2b_qp(str)
#	hex_str = binascii.b2a_hex(bin_str)
	hex_str = str.encode("utf-8").hex()

	hex_crc_temp = hex(crc_func(bin_str))
	hex_crc = hex_crc_temp[2:]

	hex_crc_full = hex_str+hex_crc+"0d"
	dec_array = []
#	Term = 13
#	for i in hex_str.decode("hex"):
#		dec_array.append(ord(i))
#
#	for j in hex_crc.decode("hex"):
#		dec_array.append(ord(j))


#	dec_array.append(Term)
	dec_array = [int(hex_crc_full[i:i+2],16) for i in range(0,len(hex_crc_full),2)]
	
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

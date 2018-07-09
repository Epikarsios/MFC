import binascii
import crcmod.predefined

crc_func = crcmod.predefined.mkCrcFun("crc-ccitt-false")

str = "Sinv2.000"
print(str)


out = binascii.a2b_qp(str)

print("Function: b2a_hex")
out3 = binascii.b2a_hex(out)
print(out3)

print("function: hexlify")
out4 = binascii.hexlify(out)
print(out4)

crc_b = crc_func(out)
print(crc_b)




print("str.encode")
hexmsg = str.encode("utf-8").hex()
print(hexmsg)
tt = hex(crc_b)
print(tt)


t = tt[2:]
print(t)

tat = hexmsg+tt+ "0d"
print(tat)

dec_array =[]
for i in tat:
#	dec_array.append(ord(int(tat[i])))
	#dec_array.append(ord(i))
	print(i)
print(dec_array)
#j = int(tat,16)
#print(j)

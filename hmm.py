#import binascii
msg = '2153657466302e313188c30d'
tmp = "Sinv2.000"
#for i in msg.decode("hex"):
#	print(i)
hex = msg
formatted_hex = ':'.join(hex[i:i+2] for i in range(0, len(hex), 2))
print(formatted_hex)




x = [int(msg[j:j+2],16)for j in range(0,len(msg),2)] # this seperates the hex string two digits at a time to decimal array

print(x)

import time

t = time.time()
s = str(t)
spac = ", "

c =  open("aaa.txt", "a")
c.write(spac)
c.write(s)
c.close()

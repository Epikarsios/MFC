import time
from dataLogger import dataLogger


log = dataLogger()


path_filename = log.create_filename()

for i in range(10):
	log.write_file(path_filename)
	time.sleep(4)


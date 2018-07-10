import time
import datetime


#now = datetime.datetime.now()      # Used to name the file with the date

#now_str = str(now)

#path_filename = "Logs/" + now_str + ".txt"
#datlog_file =str( "/Logs/"+ now+".txt")

#epoch_time =time.time()
#epoch_time_str = str(epoch_time)
#f = open(path_filename,"a")
#f.write(epoch_time_str)
#f.close()


class dataLogger:


	def create_filename(self):
		now = datetime.datetime.now()
		now_str =str(now)
		path_filename ="Logs/" + now_str + ".txt"
		return path_filename

	def write_file(self,path_filename):
		epoch_time = time.time()
		epoch_time_str = str(epoch_time)
		f = open(path_filename, "a")
		f.write(", ")
		f.write(epoch_time_str)
		f.close()


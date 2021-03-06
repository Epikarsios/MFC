import sys
sys.path.insert(0,'/home/Dlab/MFC')

from MFC import MFC
import ChkUsrInputX
from dataLogger import dataLogger
import serial
from guizero import App,Text, PushButton, Window, TextBox, warn, MenuBar, yesno, Box
log = dataLogger()
flow = MFC()     #Creates instance of MFC Class containing functions for generating cmd to be sent

# s = serial.Serial('/dev/ttyUSB0')    # Creates Serial object 
log_path_name = ""
def start_logging():
	
	log_path_name = log.create_filename()
	logbox =Box(logwindow)

def log_data():
	log.write_file(log_path_name)

def log_window():
	logwindow = Window(app)
	logbutton = PushButton(logwindow, text = "Start Logging",command =start_logging  )
def counter():
	print("Worked")

def ask_to_close():
	if yesno("Exit","Do you want to quit?"):
		print('exit')
		app.destroy()
	else:
		print("no exit")

def file_Exit():
	ask_to_close()


def get_Text():                         # Function to take value of number entered

	flowtext.value = input_box.get()
	if ChkUsrInputX.chkUsrNum(flowtext.value):
		#s.write(flow.SetPoint_Write(flowtext.value))
		print("Worked")
	else:
		# Error message
		warn("Oops","Not a Valid Number.")

file_op = [ ["File",file_Exit ], ["file2", get_Text] ]
edit_op = [ ["log window", log_window], ["edit2", get_Text] ]
app = App(title="Mass Flow Control")
menuebar =MenuBar(app, ["File", "Edit"], [file_op, edit_op])
box = Box(app)
box.bg="red"
box.height =200
box.repeat(1000,counter)
#logbox.repeat(1000,log_data )
#box.tk.configure(height =200, width = 200, background = "blue")
#for child in box.tk.winfo_children():
#	child.configure(background="blue")

text1 = Text(box, text ="Hello box")
#text1.tk.configure(background="blue")
Message = Text(app, text="Sierra Instruments Micro Trak 101")
text = Text(app)
button = PushButton(app,text ="Enter",command = get_Text)
#mywindow = Window(app, title = "Flow")
mytext = Text(app,text= "The SetPoint is ")
flowtext = Text(app)
Cmd =Text(app)
input_box = TextBox(app,text = "0.000")
app.display()

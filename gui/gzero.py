#from Tkinter import *
import sys
sys.path.insert(0,'/home/Dlab/MFC')
from MFC import MFC
import serial
from guizero import App,Text, PushButton, Window, TextBox

flow = MFC()
s = serial.Serial('/dev/ttyUSB0')
myarray = [33,83,101,116,102,48,46,48,49,49,136,195,13]
def get_Text():
	flowtext.value = input_box.get()
	


	s.write(flow.SetPoint_Write(flowtext.value))

app = App(title="Mass Flow Control")

Message = Text(app, text="Sierra Instruments Micro Trak 101")
text = Text(app)
button = PushButton(app,text ="Enter",command = get_Text)
#mywindow = Window(app, title = "Flow")
mytext = Text(app,text= "The SetPoint is ")
flowtext = Text(app)
Cmd =Text(app)
input_box = TextBox(app,text = "0.000")
app.display()

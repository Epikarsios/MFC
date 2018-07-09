from Tkinter import *
import sys
sys.path.insert(0,'/home/Dlab/MFC')
from MFC import MFC

from guizero import App,Text, PushButton, Window, TextBox

flow = MFC()

def say_hi():
	text.value = "hi "

def get_Text():
	flowtext.value = input_box.get()
	Cmd.value =flow.SetPoint_Write(flowtext.value) 
app = App(title="Mass Flow Control")

Message = Text(app, text="Sierra Instruments Micro Trak 101")
text = Text(app)
button = PushButton(app,text ="Enter",command = get_Text)
mywindow = Window(app, title = "Flow")
mytext = Text(mywindow,text= "The SetPoint is ")
flowtext = Text(mywindow)
Cmd =Text(mywindow)
input_box = TextBox(app,text = "0.000")
app.display()

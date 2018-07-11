import sys
sys.path.insert(0, '/home/Dlab/MFC')
#sys.path.insert(0,',/home/Dlab/MFC/Lib/')
from guizero import App, Text, PushButton, Window, Box, TextBox
from dataLogger import dataLogger
log = dataLogger()
file_name = ""


def test1():

	if file_name != "":
		print("Test1")
		print(file_name)
		log.write_file(file_name)
	else:
		return False
def namefile():
	global file_name
	file_name = log.create_filename()
	logbox =Box(gui)
	logbox.repeat(3000, test1)


def test2():
	global file_name
	print("Test2")
	win2 = Window(gui, title = "test2")
	file_name = log.create_filename()
	win2b = PushButton(win2, text = "push", command = namefile )
	
#	print("test 2 ", file_name)
#	win2b.repeat(3000, test1)





gui = App(title ="Flow")
but1 = PushButton(gui,text ="Open win", command = test2)
#win2but = PushButton(win2, text = "Push")
gui.display()

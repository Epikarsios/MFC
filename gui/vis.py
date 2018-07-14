import sys
sys.path.insert(0,'/home/Dlab/MFC')
from MFC import MFC
import serial
from guizero import App, TextBox,  Box, PushButton, Text, Window, MenuBar, warn, yesno, ListBox
from dataLogger import dataLogger
#from gas_to_moles import moles_to_ccm
import  ChkUsrInputX
import binascii


file_name = ""
log = dataLogger()
logbool = 1
flow = MFC()
CR =b'\r'
s = serial.Serial('/dev/ttyUSB0')



def get_flow_Rate():
	s.write(flow.Flow_Read())

	a = s.read_until(CR)
	print("read until cr  ", a)

	a_hex =  binascii.hexlify(a)    ## turns in to byte  b''  hex
	# print("hexlify", a_hex)

	a_hex_str = str(a_hex)
	# print("str(a_hex) a_hex", a_hex_str)

	str_hex =  a_hex_str[2:-7]
	# print("Change length", str_hex)

	un_hex = binascii.unhexlify(str_hex)
#	print("unhexlify", un_hex)

	un_hex_str = str(un_hex)
	print("String unhex", un_hex_str)

	value = un_hex_str[6:-1]
	#  print("Value =", value)

	fValue = float(value)
	print("Flow Rate is ",fValue)
	flow.set_flow_Rate(fValue)











## Log Functions
def enable_Log():	# Opens Logging Window
	logWin.show()
	logWin.enable()


def close_Log():	# Closes Logging Window
	logWin.disable()
	logWin.hide()

def prime_log():
	global file_name
	file_name =log.create_filename()
#	logBox = Box(gui)
	logBox.enable()
	logBox.repeat(3000, RUN_log)
#	if  logbool == 0:
#		print("destroy")
#		logBox.destroy()
#	elif logbool ==1:
#		logBox.enable()
def RUN_log():
	if file_name != "":
	
		print("writing to log")
		log.write_file(file_name)
	else:
		return False


## Gui Functions
def ask_to_close():     # Propmts User before Program Exits
	if yesno("Exit", "Do you want to quit?"):
		gui.destroy()
	else:
		return

## Eperiment Functions

          # Begin Experiment Configuration   Starts with choosing Gas

def close_Exp_Conf():
	exp_Window.disable()
	exp_Window.hide()
	gui.show()
def select_gas():

	print("select gas")
	gasBox.enable()
	gasBox.show()
	moleBox.disable()
	moleBox.hide()
	exp_Window.show()
	exp_Window.enable()
def set_gas():
	flow.set_Gas(gas_list.value)


def select_moles():
	set_gas()

	gasBox.disable()
	print("Moles")
	gasBox.hide()

	flowBox.disable()
	flowBox.hide()

	gas_text.value = flow.gas_Type
	moleBox.enable()
	moleBox.show()


def set_moles():
	if ChkUsrInputX.chkUsrNumMole(enter_moles_textbox.value):
		flow.set_Moles(enter_moles_textbox.value)
		flow.moles_to_ccm()
		select_flow()
	else:
		warn("Oops", "Not a Valid Number")


		select_moles()
		print("hide moles")
def select_flow():
	confirmBox.disable()
	confirmBox.hide()
	moleBox.disable()
	moleBox.hide()
	ccm_gas_text.value =flow.volume
	flowBox.enable()
	flowBox.show()

def set_flow():
	if ChkUsrInputX.chkUsrNumSetPoint(flow_rate_textbox.value):
		print(flow_rate_textbox.value)
		flow.set_Exp_flow_Rate(flow_rate_textbox.value)
	else:
		warn("Oops", "Not a Valid Number")
		select_flow()
def set_units():
	flow.set_Units(exp_units_list.value)
	print("set units gui")
	print(exp_units_list.value)
def confirm_Experiment():
	set_flow()
	set_units()
	flowBox.disable()
	flowBox.hide()
	confirm_moles_text.value = flow.moles
	confirm_flow_rate_text.value = flow.Exp_flow_Rate


	confirm_time_est_text.value = flow.time_Estimated_str

	confirmBox.enable()
	confirmBox.show()
def RUN_Experiment():
	global logbool
	confirmBox.disable()
	confirmBox.hide()
	close_Exp_Conf()
	print("Running")
#	prime_log()


	progress_Win.enable()
	progress_Win.show()

	abort_exp_button.enable()
	abort_exp_button.show()
	logbool = 1


	flowCmd = flow.SetPoint_Write(flow.Exp_flow_Rate)
	s.write(flowCmd)

	flow.create_filename()
	updateBox =Box(progressBox)
	updateBox.repeat(2000,Update_Progress)
def Update_Progress():
	get_flow_Rate()
	flowrate_text.value = flow.flow_Rate
	flow.write_file()

	time_remain_text.value = flow.time_Remaining_str
	volume_remain_text.value = flow.volume_Remaining_str
	if flow.volume_Remaining <= 0.001:
		STOP_Flow()
		progress_Win.destroy()
		finished_Win.enable()
		finished_Win.show()

def STOP_Flow():
	s.write(flow.SetPoint_Write("0.000"))
	print("Stop Flow")
	
def ABORT_Experiment():

	global logbool
	s.write(flow.SetPoint_Write("0.000"))    ##  Set Flow to Zero on Abort
	progress_Win.disable()
	progress_Win.hide()
#	progressBox.cancel(Update_Progress)
	progressBox.disable
	progressBox.hide()
	progress_Win.destroy()
	progressBox.destroy()
	logbool= 0
	print(logbool)
	logBox.destroy()
	gui.show()
gui = App(title = "Micro Trak 101 Mass Flow Controller", height = 300, width = 500)   # Creates Main Window Object

## Logger Widgets
logWin =Window(gui, title = "Log Window", visible = 0)        #  Creates  Log Window Object
logWin.disable()
#openLogWinButton = PushButton(gui, text ="Log Win", command =enable_Log )   # PushButton to open Log Window  for Gui Window

closeLog_logwin_button = PushButton(logWin, text ="Close Log", command = close_Log )   # PushButton to close log for Log Window

## Eperiment Widgets
exp_Window = Window(gui, title = "Experiment",height=300, width = 500, visible = 0)

                    ## Choose Gas Widgests

gasBox = Box(exp_Window, visible = 0)
gas_list = ListBox(gasBox, items =["Air", "Oxygen", "Hydrogen", "Nitrogen"], selected = "Air", scrollbar = True)
select_gas_button = PushButton(gasBox, text = "Next",command = select_moles)
cancel_exp_button = PushButton(gasBox, text = "Cancel" , command = close_Exp_Conf)
		    ## Choose micro moles
moleBox = Box(exp_Window, visible = 0)
gas_text =Text(moleBox, text = "" )
enter_moles_button = PushButton(moleBox, text = "Next", command = set_moles)
enter_moles_textbox =TextBox(moleBox,text = 0)
back_moles_button  = PushButton(moleBox, text = "Back", command = select_gas)

		 ## Choose flow rate

flowBox = Box(exp_Window, visible = 0)
ccm_gas_text = Text(flowBox, text = 0 )
exp_units_list = ListBox(flowBox, items = [ "scc/s", "scc/m", "kg/m", "g/m"], selected = "scc/m", scrollbar = True  )
back_flow_button = PushButton(flowBox, text = "Back",command = select_moles )
confirm_exp_button = PushButton(flowBox, text = "Confirm", command = confirm_Experiment)
flow_rate_textbox = TextBox(flowBox, text = 0.100  )

		## Confirm Experiment ##
confirmBox = Box(exp_Window, visible = 0)
RUN_button = PushButton(confirmBox, text = "Run", command = RUN_Experiment)
confirm_flow_rate_text = Text(confirmBox)
confirm_back_button = PushButton(confirmBox, text = "Back", command = select_flow)
confirm_moles_text = Text(confirmBox)
confirm_time_est_text = Text(confirmBox)

		## Experiment Progres Window

progress_Win = Window(gui,height = 300 , width = 500, title = "Experiment Progress", visible = 0)
progressBox = Box(progress_Win)
abort_exp_button = PushButton(progressBox, text= "Abort Experiment",command = ABORT_Experiment)
time_remaining_str = Text(progressBox, text = "Estimated Time Remaining ")
time_remain_text = Text( progressBox)
volume_remaining_str = Text(progressBox, text = "Volume Remaining ")
volume_remain_text = Text(progressBox)
logBox = Box(gui, enabled = 0)
flowrate_str = Text(progressBox, text = "Flow Rate is ")
flowrate_text = Text(progressBox)

		## Finished win
finished_Win = Window(gui, title = "Operation Complete", visible = 0)




## MenuBar Widigets
File_options = [["Prepare Experiment", select_gas], ["Exit", ask_to_close] ]
DataLog_options = [ ["Open Log", enable_Log ] ]


menuBar = MenuBar(gui, ["File", "DataLog"], [File_options, DataLog_options])


gui.display()


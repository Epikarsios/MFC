import sys
sys.path.insert(0,'/home/Dlab/MFC')
from guizero import App, TextBox,  Box, PushButton, Text, Window, MenuBar, warn, yesno, ListBox
from dataLogger import dataLogger
from gas_to_moles import moles_to_ccm



## Log Functions
def enable_Log():	# Opens Logging Window
	logWin.show()
	logWin.enable()


def close_Log():	# Closes Logging Window
	logWin.disable()
	logWin.hide()


## Gui Functions
def ask_to_close():     # Propmts User before Program Exits
	if yesno("Exit", "Do you want to quit?"):
		gui.destroy()
	else:
		return

## Eperiment Functions

def Run_Exp_Conf():          # Begin Experiment Configuration   Starts with choosing Gas
	close_select_moles()
	exp_Window.show()
	exp_Window.enable()
	cancel_exp_button.enable()
	cancel_exp_button.show()
	select_gas_button.enable()
	select_gas_button.show()
	exp_Gas_list.enable()
	exp_Gas_list.show()
def close_Exp_Conf():
	exp_Window.disable()
	exp_Window.hide()

def close_select_gas():
	cancel_exp_button.disable()
	cancel_exp_button.hide()
	select_gas_button.disable()
	select_gas_button.hide()
	exp_Gas_list.disable()
	exp_Gas_list.hide()
	
#def select_gas():
#	print("gas")

def select_moles():
	close_select_gas()
	close_select_flow()
	enter_moles_button.enable()
	enter_moles_button.show()
	enter_moles_textbox.enable()
	enter_moles_textbox.show()
	back_moles_button.enable()
	back_moles_button.show()
	exp_Gas_text.value = exp_Gas_list.value
	exp_Gas_text.show()
	enter_moles_textbox.show()

def close_select_moles():
	enter_moles_button.disable()
	enter_moles_button.hide()
	enter_moles_textbox.disable()
	enter_moles_textbox.hide()
	back_moles_button.disable()
	back_moles_button.hide()
def select_flow():
	
	close_select_moles()

	## Enable and Show new widgets
	exp_units_list.enable()
	ccm_gas_text.enable()
	ccm_gas_text.show()
	exp_units_list.show()

	ccm_gas_text.value = moles_to_ccm(enter_moles_textbox.value, exp_Gas_list.value) 
	run_exp_button.enable()
	run_exp_button.show()
	back_flow_button.enable()
	back_flow_button.show()
def close_select_flow():
	exp_units_list.disable()
	exp_units_list.hide()
	ccm_gas_text.disable()
	ccm_gas_text.hide()
	back_flow_button.disable()
	back_flow_button.hide()
	run_exp_button.disable()
	run_exp_button.hide()
def RUN_Experiment():
	close_select_flow()
	print("Running")








gui = App(title = "vis non vis", height = 300, width = 300)   # Creates Main Window Object

## Logger Widgets
logWin =Window(gui, title = "Log Window", visible = 0)        #  Creates  Log Window Object
logWin.disable()
openLogWinButton = PushButton(gui, text ="Log Win", command =enable_Log )   # PushButton to open Log Window  for Gui Window

closeLog_logwin_button = PushButton(logWin, text ="Close Log", command = close_Log )   # PushButton to close log for Log Window

## Eperiment Widgets
exp_Window = Window(gui, title = "Experiment",height=300, width = 500, visible = 0)

                    ## Choose Gas Widgests
exp_Gas_list = ListBox(exp_Window, items =["Air", "Oxygen", "Hydrogen", "Nitrogen"], selected = "Air",visible = 0, scrollbar = True)
select_gas_button = PushButton(exp_Window, text = "Next",command = select_moles, visible = 0)
cancel_exp_button = PushButton(exp_Window, text = "Cancel" , command = close_Exp_Conf, visible = 0)
		    ## Choose micro moles
exp_Gas_text =Text(exp_Window, text =exp_Gas_list.value, visible = 0 )
enter_moles_button = PushButton(exp_Window, text = "Next", command = select_flow, visible = 0)
enter_moles_textbox =TextBox(exp_Window,text = 0, visible =0)
back_moles_button  = PushButton(exp_Window, text = "Back", command = Run_Exp_Conf, visible = 0)

		 ## Choose flow rate
ccm_gas_text = Text(exp_Window, text =" 0", visible = 0 )
exp_units_list = ListBox(exp_Window, items = [ "ssc/s", "ssc/m", "kg/m", "g/m"], selected = "ssc/m", scrollbar = True, visible = 0  )
back_flow_button = PushButton(exp_Window, text = "Back",command = select_moles, visible = 0 )
run_exp_button = PushButton(exp_Window, text = "Run", command = RUN_Experiment, visible = 0)

## MenuBar Widigets
File_options = [["Prepare Experiment", Run_Exp_Conf], ["Exit", ask_to_close] ]
DataLog_options = [ ["Open Log", enable_Log ] ]


menuBar = MenuBar(gui, ["File", "DataLog"], [File_options, DataLog_options])


gui.display()


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

def Run_Exp_Conf():
	exp_Window.show()
	exp_Window.enable()
	ccm_gas_text.disable()
def select_gas():
	print("gas")

def select_mass():
	exp_Gas_list.disable()
	exp_Gas_list.hide()
	select_gas_button.disable()
	select_gas_button.hide()
	select_mass_button.enable()
	select_mass_button.show()
	print(exp_Gas_list.value)

	exp_Gas_text.value = exp_Gas_list.value
	exp_Gas_text.show()
	enter_moles_textbox.show()

def select_flow():
	print("flow")
	select_mass_button.disable()
	select_mass_button.hide()
	enter_moles_textbox.disable()
	enter_moles_textbox.hide()
	exp_units_list.enable()
#	ccm_gas_test.value = "high"
	ccm_gas_text.enable()
	ccm_gas_text.show()
	exp_units_list.show()
	print(enter_moles_textbox.value)
	print("ccm", ccm_gas_text.value)
	ccm_gas_text.value = moles_to_ccm(enter_moles_textbox.value, exp_Gas_list.value)
#	ccm_gas_text.value = "hey"
	print(moles_to_ccm(enter_moles_textbox.value, exp_Gas_list.value))



def select_units():
	print("units")


gui = App(title = "vis non vis", height = 300, width = 300)   # Creates Main Window Object

## Logger Widgets
logWin =Window(gui, title = "Log Window", visible = 0)        #  Creates  Log Window Object
logWin.disable()
openLogWinButton = PushButton(gui, text ="Log Win", command =enable_Log )   # PushButton to open Log Window  for Gui Window

closeLog_logwin_button = PushButton(logWin, text ="Close Log", command = close_Log )   # PushButton to close log for Log Window

## Eperiment Widgets
exp_Window = Window(gui, title = "Experiment",height=300, width = 500, visible = 0)
exp_Gas_list = ListBox(exp_Window, items =["Air", "Oxygen", "Hydrogen", "Nitrogen"], selected = "Air", command = select_gas, scrollbar = True)

select_gas_button = PushButton(exp_Window, text = "Next",command = select_mass)


exp_Gas_text =Text(exp_Window, text =exp_Gas_list.value, visible = 0 )
exp_units_list = ListBox(exp_Window, items = [ "ssc/s", "ssc/m", "kg/m", "g/m"], selected = "ssc/m",command = select_units, scrollbar = True, visible = 0  )
select_mass_button = PushButton(exp_Window, text = "Next", command = select_flow, visible = 0)
enter_moles_textbox =TextBox(exp_Window,text = 0, visible =0)

ccm_gas_text = Text(exp_Window, text =" 0" )


## MenuBar Widigets
File_options = [["Prepare Experiment", Run_Exp_Conf], ["Exit", ask_to_close] ]
DataLog_options = [ ["Open Log", enable_Log ] ]


menuBar = MenuBar(gui, ["File", "DataLog"], [File_options, DataLog_options])


gui.display()


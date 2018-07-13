from guizero import App, Box,  TextBox, Text, PushButton, Window, ListBox

import sys
sys.path.insert(0,'/home/Dlab/MFC')
from MFC import MFC

flow = MFC()



def set_gas():
	flow.set_Gas(gas_list.value)


def select_moles():
	gasbox.hide()
	set_gas()
	molebox.show()

def set_moles():
	flow.set_Moles(mole_text.value)
	flow.moles_to_ccm()
	print(flow.volume)
def select_flow():

	set_moles()
	molebox.hide()
	flowbox.show()
	flowbox.enable()
	flowtext = Text(flowbox,text = flow.volume)

win = App( title = "Test")


gasbox = Box(win)
molebox = Box(win, visible =0)

flowbox = Box(win, visible=0)
flowbox.disable()
gas_list = ListBox(gasbox, items = ["Oxygen"])

but = PushButton(gasbox, text= 'next', command = select_moles)


mole_text = TextBox(molebox )

but2 = PushButton(molebox, text= "next", command = select_flow)



win.display()

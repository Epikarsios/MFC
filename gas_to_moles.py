T = float(298) # Kelvin
density_air     = float(0.001275)

density_oxygen  =float( 0.001429) # grams per cm ^3
density_hydrogen = float(0.0000899)

density_nitrogen = float(0.001251)

molarmass_oxygen = float(15.999) # grams per mol
molarmass_air = float(28.96)
molarmass_nitrogen =float(28.014)
molarmass_hydrogen = float(2.016)
R =  float(0.0821)   # atm*L/mol*K
def moles_to_ccm( Moles,Gas):

	molarmass= 0
	density = 0
	if  Gas =="Oxygen":
		density = density_oxygen
		molarmass = molarmass_oxygen
	elif Gas == "Nitrogen":
		density = density_nitrogen
		molarmass = molarmass_nitrogen
	elif Gas == "Hydrogen":
		density = density_hydrogen
		molarmass = molarmass_hydrogen
	elif Gas == "Air": 
		density = density_air
		molarmass = molarmass_air

	uMoles = float(Moles)*(0.000001)
	grams =	float(uMoles) * molarmass
	cubic_centimeters = grams / density
	return cubic_centimeters


def time_of_flow(vol, units):
	
	if units == "scc/m":
		sec_total =vol/60
		if sec_total >= 60:
			mins = sec_total/60
			return mins
		else:
			sec = sec_total 
			return sec

def  get_Pressure(Volume, Moles):
	pressure =( Moles * R * T)/ Volume
	return pressure

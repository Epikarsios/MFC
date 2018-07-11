
density_air     = 1000

density_oxygen  =float( 0.001429) # grams per cm ^3
density_hydrogen = 1000

density_nitrogen = 1000

molarmass_oxygen = float(15.999) # grams per mol



def moles_to_ccm( Moles,Gas):
	
	if  Gas =="Oxygen":
		density = density_oxygen
		molarmass = molarmass_oxygen
	elif Gas == "Nitrogen":
		density = density_nitrogen
	#	molarmass = molarmass_nitrogen
	elif Gas == "Hydrogen":
		density = density_hydrogen
	elif Gas == "Air": 
		density = density_air
	uMoles = float(Moles)*(0.000001)
	grams =	float(uMoles) * molarmass
	cubic_centimeters = grams / density
	return cubic_centimeters

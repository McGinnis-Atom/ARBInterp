from __future__ import division
import numpy as np
from ARBTools.ARBInterp import tricubic
from ARBTools.ARBTrajec import trajectories

############################### Skookum ###############################
	
if __name__ == '__main__':
	mAr = 39.948		# Mass Ar
	N = 100		# number of atoms
	T = 0.04		# temperature in K

	moment = 3	#	magnetic moment in Bohr magnetons - mJ x g-factor
	# testing with Ar in 3P2 state = mJ = 2, low-field-seeking
	
	tmax = 0.01	# end time of simulation
	timestep = 1e-6 # really should be 1e-7 for very accurate work but larger steps OK for testing

	fieldname = "ExampleTrapField"
	field = np.genfromtxt(fieldname+'.csv', delimiter=',') # field to be interpolated
	
	ArTest = trajectories(field, mAr, moment) # creates class to iterate particle trajectories
	ArSample = ArTest.atoms(T,N)	# creates random sample of Ar atoms
	np.savetxt('Rand_In.csv', ArSample, delimiter=',')	# Save initial sample to file
	
	ArTest.Iterate(ArSample, tmax, timestep)	# tracks motion of particles through field for some time

	np.savetxt('Rand_Out.csv', ArSample, delimiter=',')	# Save final sample to file
#Reads .csv of spectra data from Open Supernova Catalogue and generates a spectrum

import numpy as np

#Load .csv into numpy array
specdata = np.loadtxt('1987AspecU.csv', delimiter=",", skiprows=1)

#Handles for x and y solumns
time = specdata[:,1]
magnitude = specdata[:,2]

#Grab pylab
import pylab as plt

#Create plot of magnitude vs. time
plt.plot(time, magnitude)
plt.xlabel('Time(s)')
plt.ylabel('Magnitude')
plt.title('Magnitude vs. time in the U band of 1987A')
plt.grid(True)

plt.savefig("U_magvstime_matplotlib.png")


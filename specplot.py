#Reads .csv of spectra data from Open Supernova Catalogue and generates a spectrum

import numpy as np

#Load .csv into numpy array
specdata = np.loadtxt('1987Aspec.csv', delimiter=",", skiprows=1)

#Handles for x and y solumns
time = specdata[:,1]
magnitude = specdata[:,2]

#Grab pylab
import pylab as plt

plt.plot(time, magnitude)
plt.xlabel(Time

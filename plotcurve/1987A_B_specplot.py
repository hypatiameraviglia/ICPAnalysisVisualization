#Reads .csv of spectra data from Open Supernova Catalogue and generates a spectrum

import numpy as np

#Load .csv into numpy array
specdata = np.loadtxt('1987AspecB.csv', delimiter=",", skiprows=1)

#Print array shape
print("Shape of array =", np.shape(specdata))

#Handles for x and y solumns
time = specdata[:,0]
magnitude = specdata[:,1]

#Grab pylab
import pylab as plt

#Create plot of magnitude vs. time
plt.plot(time, magnitude)
plt.xlabel('Time(s)')
plt.ylabel('Magnitude')
plt.title('Magnitude vs. time in the B band of 1987A')
plt.grid(True)

plt.savefig("B_magvstime_matplotlib.png")


#Reads .csv of spectra data from Open Supernova Catalogue and generates a spectrum
import numpy as np
import pylab as plt

#Load .csv into numpy array
U = np.loadtxt('2014JspecU.csv', delimiter=",", skiprows=1)
B = np.loadtxt('2014JspecB.csv', delimiter=',', skiprows=1)
V = np.loadtxt('2014JspecV.csv', delimiter=',', skiprows=1)
R = np.loadtxt('2014JspecR.csv', delimiter=',', skiprows=1)
I = np.loadtxt('2014JspecI.csv', delimiter=',', skiprows=1)

#Handles for x and y solumns
timeU = U[:,0]
magU = U[:,1]
timeB = B[:,0]
magB = B[:,1]
timeV = V[:,0]
magV = V[:,1]
timeR = R[:,0]
magR = R[:,1]
timeI = I[:,0]
magI = I[:,1]

#Create plot of magnitude vs. time with all data sets
plt.plot(timeU, magU, color='olivedrab', label='U band')
plt.plot(timeB, magB, color='darkgreen', label='B band')
plt.plot(timeV, magV, color='teal', label='V band')
plt.plot(timeR, magR, color='steelblue', label='R band')
plt.plot(timeI, magI, color='darkblue', label='I band')

plt.xlabel('Time(s)')
plt.ylabel('Magnitude')
plt.title('Comparing bands of 2014J in magnitude vs. time')
plt.grid(True)
plt.legend()

plt.savefig("2014J_all_magvstime.png")


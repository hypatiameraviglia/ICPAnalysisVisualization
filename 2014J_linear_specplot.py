#Reads .csv of spectra data from Open Supernova Catalogue and generates a spectrum
import numpy as np
import pylab as plt
import scipy

#Load .csv into numpy array
U = np.loadtxt('2014JlinearU.csv', delimiter=",", skiprows=1)

#Handles for x and y solumns
time = U[:,0]
mag = U[:,1]

#Create plot of magnitude vs. time with all data sets
plt.plot(time, mag, color='darkblue', label='2014J')

plt.xlabel('Time(s)')
plt.ylabel('Magnitude')
plt.title('Post-cooling, pre-plateau rise of 2014J band U in magnitude vs. time')
plt.grid(True)

#Create linear fit
linear=np.polyfit(time, mag, 1)

#Plot linear fit
linear_fn=np.poly1d(linear)
x_s = np.arange(56700,56720)
plt.plot(x_s, linear_fn(x_s), color="forestgreen")

#Use scipy to print slope, intercept, etc.
from scipy.stats import linregress
slope = linregress(time,mag)
print(slope)

plt.legend()

plt.savefig("2014J_U_linear_matplotlib.png")


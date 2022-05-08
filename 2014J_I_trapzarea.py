#Reads .csv of spectra data from Open Supernova Catalogue and generates a spectrum
import numpy as np

#Load .csv into numpy array
specdata = np.loadtxt('data/2014JspecI.csv', delimiter=",", skiprows=2)

#Print array shape
print("Shape of array =", np.shape(specdata))

#Handles for x and y solumns
time = specdata[:,0]
magnitude = specdata[:,1]

#Calculate area using trapezoidal method
def trapezoidal(time, magnitude):
    total = 0
    i = 0
    if len(time) != len(magnitude):
        raise IndexError("time and magnitude are not the same length")
    
    print(len(time))

    for i in range((len(time)) - 1):
        #total = total + ((time[i+1] - time[i])*(magnitude[i]) + (0.5)*(time[i+1] - time[i])*(abs(magnitude[i+1] - magnitude[i])))
        total += (time[i+1] - time[i])*0.5*(magnitude[i+1] + magnitude[i])
    return(total)

#Run function
total = trapezoidal(time, magnitude)
print(total)

#Check area with numpy trapz
checkarea = 0
checkarea = np.trapz(magnitude, time)
print(checkarea)



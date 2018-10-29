"""
Checkpoint 6 - DAH - 2018
"""

import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
import pylab as pl
import math

#imports data 
dataFile = open("upsilons-mass-xaa.txt","r")
lines = dataFile.readlines()
dataFile.close()

#fiters data and adds to list
masses = []
for i in range(len(lines)):
    masses.append(float(lines[i].strip('\n')))

#sets number of bins for plot
noOfBins = 350

#plots histogram
entries, binedges,patches = pl.hist(masses,bins= noOfBins)
pl.title("Histogram of masses")
pl.xlabel("Masses [GeV/c^2]")
pl.ylabel("Frequency")
pl.show()

#peak ranges
massesOne = []
massesTwo = []
massesThree = []


#splits masses into 3 peaks lists
for i in range(len(masses)):
	if 9.43<masses[i]<9.48:
		massesOne.append(masses[i])
	elif 10.28<masses[i]<10.44:
		massesThree.append(masses[i])
	elif 9.92<masses[i]<10.11:
		massesTwo.append(masses[i])		

#bins data for peaks
entries1, binedges1, patches1 = pl.hist(massesOne, bins = 50)
entries2, binedges2, patches2 = pl.hist(massesTwo, bins = 50)
entries3, binedges3, patches3 = pl.hist(massesThree, bins = 50)

#gets max bin for each particle
maxBin1 = max(entries1)
maxBin2 = max(entries2)
maxBin3 = max(entries3)

#list for masses of three peaks
mesonMasses = []

#works out masses and appends to list
for i in range(len(entries1)):
	if entries1[i] == maxBin1:
		mesonMasses.append((binedges1[i+1] + binedges1[i])/2)
for i in range(len(entries2)):
	if entries2[i] == maxBin2:
		mesonMasses.append((binedges2[i+1] + binedges2[i])/2)
for i in range(len(entries3)):
	if entries3[i] == maxBin3:
		mesonMasses.append((binedges3[i+1] + binedges3[i])/2)

#calculates and prints differences in masses	
#print mesonMasses
#print "2S - 1S = " + str(mesonMasses[1] - mesonMasses[0]) + " GeV/c^2"
#print "3S - 1S = " + str(mesonMasses[2] - mesonMasses[0]) + " GeV/c^2"

masses1 = []
for i in range(len(masses)):
	if 9.4<masses[i]<9.6:
		masses1.append(masses[i])
mean = np.mean(masses1)
variance = np.var(masses1)
stddev = np.std(masses1)
stddevofmean = stddev/(math.sqrt(len(masses1)))
print "The mean is " +str(mean)
print "The variance is " +str(variance)
print "The standard deviation is " +str(stddev)
print "The standard deviation on the mean is " +str(stddevofmean)


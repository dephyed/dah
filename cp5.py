"""
Checkpoint 5 - DAH - 2018
"""

#from webiopi.devices.sensor.onewiretemp import DS18S20
import datetime
import pylab as pl
import matplotlib.animation as animation
import math
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error

serialNumber1 = "aSerialNumber"
serialNumber2 = "anotherSerialNumber"
timeValues = []
measurements1 = []
measurements2 = []
plotFigure = pl.figure()

def measureTemp(serial):
	#t = DS18S20(slave=serial)
	#temp = t.getCelsius()
	#return temp
	return serial**2
#testing method	
def measureTemp2(serial):
	return serial**2.001
	
def partTwo():
	plotPartTwo()
	
def partThree():
	plotPartThree()
	bins = np.linspace(min(measurements1), max(measurements1), 5)
	plt.hist([measurements1, measurements2], bins,  label=['Sensor 1', 'Sensor 2'], color=['b','r'])

	plt.legend(loc='upper right')
	plt.title('Histogram of Temperature Readings in Celsius from 2 Different Nearby Sensors')
	plt.xlabel('Temperature [degrees Celsius]')
	plt.ylabel('Frequency')
	plt.show()
	
	difference = []
	for i in range(len(measurements1)):
		difference.append(measurements1[i]-measurements2[i])
	
	plt.plot(timeValues, difference)
	plt.title('Graph showing difference in temperatre \nbetween two sensors vs time')
	plt.xlabel('Time [s]')
	plt.ylabel('Difference in temperature between sensors [degrees Celsius]')
	plt.show()
	
	rmsVal = rms(measurements1, measurements2)
	print rmsVal
	

def plotPartThree():
	ani = animation.FuncAnimation(plotFigure, updatePlotPartThree, interval = 200)
	fig = pl.gcf()
	fig.canvas.set_window_title('Tom is a lesbian')
	pl.title('Graph showing temperature vs time for two temperature sensors')
	pl.xlabel('Time [hh:mm:ss]')
	pl.ylabel('Temperature [degrees Celsius]')
	pl.show()
	

def plotPartTwo():
	ani = animation.FuncAnimation(plotFigure, updatePlotPartTwo, interval = 2500)
	fig = pl.gcf()
	fig.canvas.set_window_title('Tom is a lesbian')
	
	pl.show()

def updatePlotPartTwo(i):
	timeValues.append(datetime.datetime.now())
	#measurements.append(measureTemp(serial))
	measurements1.append(measureTemp(i))		
	plotFigure.clear()
	pl.title('Graph showing temperature vs time for a temperature sensor')
	pl.xlabel('Time [hh:mm:ss]')
	pl.ylabel('Temperature [degrees Celsius]')
	pl.plot(timeValues, measurements1)


def updatePlotPartThree(i):
	timeValues.append(datetime.datetime.now())
	#measurements.append(measureTemp(serial))
	measurements1.append(measureTemp(i))	
	measurements2.append(measureTemp2(i))	
	plotFigure.clear()
	pl.title('Graph showing temperature vs time for two temperature sensors')
	pl.xlabel('Time [hh:mm:ss]')
	pl.ylabel('Temperature [degrees Celsius]')
	pl.plot(timeValues, measurements1, label='Sensor 1', color='r')
	pl.plot(timeValues, measurements2, label='Sensor 2', color='b')
	pl.legend()
	
def rms(x,y):
	rms = math.sqrt(mean_squared_error(x, y))
	return rms
	
def main():
	partThree()
	
main()

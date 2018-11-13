"""
DAH Project 2018

FFT analyser 
"""

import serial
import numpy as np
import time
import matplotlib.pyplot as plt

#sets where the arduino is
ser=serial.Serial('/dev/ttyACM0',115200, timeout=5) 
time.sleep(0.1)

timeConversionFactor = 0.5
maxVoltage = 3.5

#function that reads data from arduino and returns numpy array of data
def read():
	ser.flushInput()
	ser.write(bytes([4,2]))
	data = ser.read(1600)
	return np.frombuffer(data, dtype=np.uint8)

#performs the fast fourier transform and returns data and list of frequencies
def transform(data):
	transformedData = np.fft.rfft(data)
	frequencyList = []
	return frequencyList, transformedData

#creates list of times from elements
def timeConvert(data, endPoint):
	timeList = []
	if endPoint != 0:
		#creates list starting from end point of last time list
		for i in range(len(data)):
			timeList.append(endPoint+(i*timeConversionFactor))
			if i == len(data):
				endpoint = endPoint+(i*timeConversionFactor)
	return timeList
	
#converts the bits from the incoming signal into a voltage based on max voltage	
def voltageConvert(data):
	maxdata = max(data)
	voltageData = []
	for i in range(len(data)):
		voltageData.append((data[i]/maxdata)*maxVoltage)
	return voltageData

#function that takes data for about 5 seconds and makes one list of data
def takeData():	
	i = 0 
	data = []
	while i<10:
		tempData = read()
		data.append(tempData.tolist())
		i+=1
	return data

#plots time and frequency domains of signal side by side
def plot(voltList, timeList, transformedData, frequencyList, end):
	plt.subplot(1,2,1)
	plt.plot(timeList, voltList)
	plt.xlabel("Time [s]")
	plt.ylabel("Voltage [V]")
	#plt.title("")
	
	plt.subplot(1,2,2)
	plt.plot( transformedData)
	plt.xlabel("Frequency [Hz]")
	plt.ylabel("Amplitude")
	#plt.title("")
	
	#if not the end, display plot but continue with code
	if end == "False":
		plt.draw()
	elif end == "True":
		plt.show()

#function that runs everything else
def main():
	repeats = 5
	totalData = []
	endPoint = 0
	for i in range(repeats):
		#reads data and appends to total list
		data = takeData()
		totalData.append(data)
		
		#converts bytes to time and amplitude to voltages
		timeList, endPoint = timeConvert(totalData, endPoint)
		voltList = voltageConvert(totalData)
		#performs fft, and get's list of frequencies
		frequencyList, transformData = transform(totalData)
		#makes plots
		if i == repeats:
			plot(voltList, timeList, transformedData, frequencyList, True)
		else:
			plot(voltList, timeList, transformedData, frequencyList, False)
	
main()

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
time.sleep(1)

timeConversionFactor = 0.000375
frequencyConversionFactor = float(1/timeConversionFactor)
maxVoltage = 5

#function that reads data from arduino and returns numpy array of data
def read():
	ser.flushInput()
	time.sleep(1)
	ser.write(bytes([4,2]))
	data = ser.read(1600)
	return np.frombuffer(data, dtype=np.uint8)

#performs the fast fourier transform and returns data and list of frequencies
def transform(data):
	tempdata = np.array(data)
	transformedData = np.fft.fft(tempdata)
	frequencyList = []
	for i in range(len(transformedData)):
		frequencyList.append(i*2*frequencyConversionFactor/len(transformedData))
	return frequencyList, transformedData

#creates list of times from elements
def timeConvert(data, endPoint):
	timeList = []
	
	#creates list starting from end point of last time list
	for i in range(len(data)):
		timeList.append(endPoint+(i*timeConversionFactor))
		if i == len(data):
			endpoint = endPoint+(i*timeConversionFactor)
	return timeList, endPoint
	
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
	while i<1:
		tempData = read()
		
		data.extend(tempData.tolist())
		i+=1
	return data

#plots time and frequency domains of signal side by side
def plot(voltList, timeList, transformedData, frequencyList,powerSpectrum):
	plt.subplot(1,3,1)
	plt.plot(timeList, voltList)
	plt.xlabel("Time [s]")
	plt.ylabel("Voltage [V]")
	
	
	plt.subplot(1,3,2)
	plt.plot(frequencyList, transformedData)
	plt.xlabel("Frequency [Hz]")
	plt.ylabel("Amplitude")
	
	plt.subplot(1,3,3)
	plt.plot(frequencyList, powerSpectrum)
	plt.xlabel("Frequency [Hz]")
	plt.ylabel("Power")
	
	plt.tight_layout()
	plt.show()

#function that runs everything else
def main():
	repeats = 10
	totalData = []
	endPoint = 0
	for i in range(repeats):
		#reads data and appends to total list
		data = takeData()
		totalData.extend(data)
		
		#converts bytes to time and amplitude to voltages
		timeList, endPoint = timeConvert(totalData, endPoint)
		voltList = voltageConvert(totalData)
		#performs fft, and get's list of frequencies
		frequencyList, transformedData = transform(totalData)
		powerSpectrum = np.square(transformedData)
		plot(totalData, timeList, transformedData, frequencyList, powerSpectrum)

main()

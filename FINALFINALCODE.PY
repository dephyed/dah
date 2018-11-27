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
maxVoltage = 5.0

#function that reads data from arduino and returns numpy array of data
def read():
	#clears buffer memory
	ser.flushInput()
	time.sleep(0.5)
	#sets sampling rate
	ser.write(bytes([4,2]))
	time.sleep(0.5)
	print("SING!")
	startTime=time.time()
	#tells arduino to read 1600 bytes
	data = ser.read(1600)
	print time.time()-startTime
	return np.frombuffer(data, dtype=np.uint8)

#performs the fast fourier transform and returns data and list of frequencies
def transform(data):
	tempdata = np.array(data)
	#performs fft
	transformedData = np.fft.fft(tempdata)
	frequencyList = []
	#calculates frequencies based on measured conversion factor
	for i in range(len(transformedData)):
		frequencyList.append(i*2*frequencyConversionFactor/len(transformedData))
	return frequencyList, transformedData

#creates list of times from elements
def timeConvert(data, endPoint):
	timeList = []
	conversionFactors =[]
	
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

#function that takes data for given repeats and makes one list of data
def takeData():	
	i = 0 
	data = []
	times = []
	while i<2:
		tempData = read()
		data.extend(tempData.tolist())
		i+=1
	print len(data)	
	return data

#plots time and frequency domains of signal side by side
def plot(voltList, timeList, transformedData, frequencyList,powerSpectrum):
	#plt.subplot(1,3,1)
	plt.plot(timeList, voltList)
	plt.xlabel("Time [s]")
	plt.ylabel("Voltage [V]")
	plt.title("Graph showing voltage versus time of an incoming signal from\n a microphone at 2000Hz\n with a Hanning Window")
	plt.show()
	
	#plt.subplot(1,3,2)
	plt.plot(frequencyList, transformedData)
	plt.xlabel("Frequency [Hz]")
	plt.ylabel("Amplitude")
	plt.title("Graph showing Fourier transform of an incoming signal from\n a microphone at 2000Hz\n with a Hanning window")
	plt.show()
	
	#plt.subplot(1,3,3)
	plt.plot(frequencyList, powerSpectrum)
	plt.xlabel("Frequency [Hz]")
	plt.ylabel("Amplitude")
	plt.title("Graph showing power spectrum of an incoming signal from\n a microphone at 2000Hz\n with a Hanning window")
	plt.show()

#writes all the data to file
def writeToFile(time, data, frequency, transformedData, power, filename):
	file = open(filename,"w")
	file.write("Data for DATA")
	file.write("Time, Voltage, Frequency, Amplitdue for Frequency, Amplitude for Power Spectrum")
	for i in range(len(time)):
		file.write(time[i] +str(", ") + data[i] +str(", ")+ frequency[i]+str(", ")+transformedData[i]+str(", ")+power[i])
		
#function that runs everything else
def main():
	repeats = 1
	totalData = []
	endPoint = 0
	for i in range(repeats):
		#reads data and appends to total list
		data = takeData()
		totalData.extend(data)
		window = np.hanning(len(totalData))
		
		finalData = totalData * window
		#converts bytes to time and amplitude to voltages
		timeList, endPoint = timeConvert(finalData, endPoint)
		voltList = voltageConvert(finalData)
		#performs fft, and get's list of frequencies
		frequencyList, transformedData = transform(finalData)
		#calculates power spectrum
		absol = np.absolute(transformedData)
		powerSpectrum = np.square(absol)
		#write to file
		filename = "sin.txt"
		writeToFile(timeList, voltList, frequencyList, transformedData, powerSpectrum, filename)
		#plot data
		plot(voltList, timeList, transformedData, frequencyList, powerSpectrum)


main()

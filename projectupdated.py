import serial
import numpy as np
import time

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
	
def transform(data):
	transformedData = np.fft.rfft(data)
	frequencyList = []
	return frequencyList, transformedData
	
def timeConvert(data):
	timeList = []
	for i in range(len(data)):
		timeList.append(i*timeConversionFactor)

def voltageConvert(data):
	maxdata = max(data)
	voltageData = []
	for i in range(len(data)):
		voltageData.append((data[i]/maxdata)*maxVoltage)
	return voltageData

def takeData():	
	i = 0 
	data = np.empty(2)
	while i<10:
		tempData = read()
		np.congregate((data,tempData) axis=None)
		i+=1
	return data


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
	
	if end == "False":
		plt.draw()
	elif end == "True":
		plt.show()

	
def main():
	repeats = int(raw_input("No. of Repeats: "))
	totalData = []
	for i in range(repeats):
		data = takeData()
		data.tolist()
		totalData.append(data)
		
		
		timeList = timeConvert(totalData)
		voltList = voltageConvert(totalData)
		frequencyList, transformData = transform(totalData)
		if i == repeats:
			plot(voltList, timeList, transformedData, frequencyList, True)
		else:
			plot(voltList, timeList, transformedData, frequencyList, False)
	
main()

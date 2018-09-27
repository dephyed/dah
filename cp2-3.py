from webiopi.devices.analog.mcp3x0x import MCP3208
from webiopi.devices.analog.mcp492X import MCP492X

ADC0 = MCP3208(chip=0)
DAC1 = MCP492X(chip=1, channelCount=2, vref=3.3)

outputVoltages = [0]
a=0
while a <= 3.3:
	a += 0.1
	outputVoltages.append(a)
	
print outputVoltages

dACChannel = int(input("DAC Channel: "))
aDCChannel = int(input("ADC Channel: "))

aDCReadings = []

file = open("Checkpoint2-3.txt","w")
file.write("This file is the data from Checkpoint 2.3 of the Data Aquisition and Handling course. \n A DAC was used to vary the input voltage to an LED placed next to a LDR connected to an ADC. \n At each output voltage, the voltage from the LDR circuit was read. The data is below.\n")
file.write("Output Voltage from DAC [V], Voltage Read from LDR Circuit [V]"

for i in range(len(outputVoltages)-1):
	DAC1.analogWriteVolt(dACChannel, outputVoltages[i])
	dac = DAC1.analogReadVolt(dACChannel)	
	adc = ADC0.analogReadVolt(aDCChannel)
	
	file.write(str(dac) + "," + str(adc))
	
	print(str(dac) + "," + str(adc))
	
	

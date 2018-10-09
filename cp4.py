"""
Checkpoint 4 - DAH - 2018
"""

import RPi.GPIO as GPIO
import  time
from  webiopi.devices.digital.pcf8574 import PCF8574A
import random



mcp = PCF8574A(slave=0x38)

# Set  which PCF8574 GPIO pin  i s  connected  to  the LED ( negative  l o g i c )
LED0 = 0
LED1 = 1
LED2 = 2
LED3 = 3
SWITCH0 = 4

leds = [LED0, LED1, LED2, LED3]

# Setup GPIOs
mcp.setFunction(LED0, GPIO.OUT) #Set  Pin  as  output
mcp.setFunction(LED1, GPIO.OUT)
mcp.setFunction(LED2, GPIO.OUT)
mcp.setFunction(LED3, GPIO.OUT)
mcp.setFunction(SWITCH0, GPIO.IN)
# Turn on  the LED f o r  the  f i r s t  time
mcp.digitalWrite(LED0, GPIO.HIGH)
mcp.digitalWrite(LED1, GPIO.HIGH)
mcp.digitalWrite(LED2, GPIO.HIGH)
mcp.digitalWrite(LED3, GPIO.HIGH)

def patternOne():
	mcp.digitalWrite(LED0, GPIO.HIGH)
	mcp.digitalWrite(LED1, GPIO.LOW)
	mcp.digitalWrite(LED2, GPIO.LOW)
	mcp.digitalWrite(LED3, GPIO.HIGH)
	while True:
		value = not GPIO.input(LED0)
		GPIO.output(LED0,value)
		GPIO.output(LED3,value)
		otherValue = not GPIO.input(LED1)
		GPIO.output(LED1,otherValue)
		GPIO.output(LED2,otherValue)
		time.sleep(2)

def patternTwo():
	#code here
	
def patternThree():
	#code here

def patternSwitch(pattern):
	patterns = [patternOne(), patternTwo(), patternThree()]
	newPattern = random.choice(patterns)
	
	while True:
		if newPattern == pattern:
			newPattern = random.choice(patterns)
		else:
			break
			
	return newPattern


def partOne():
	while True:
		value = not GPIO.input(LED0)
		GPIO.output(LED0,value)
		time.sleep(1)
		
def partTwo():
	while True:
		for i in range(len(leds)):
			GPIO.output(leds[i], GPIO.HIGH)
			time.sleep(1)
			GPIO.output(leds[i], GPIO.LOW)
			
def partThree():
	#GPIO.portWrite(value)
	currentPattern = patternOne()
	while True:
		currentPattern()
		
		if (mcp.digitalRead(SWITCH0) == GPIO.LOW):
			currentPattern = patternSwitch(currentPattern)
			mcp.digitalWrite(SWITCH0, GPIO.HIGH)
	
	
def main():
	partOne()
	partTwo()
main()

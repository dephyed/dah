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
	startTime = time.time()
	mcp.digitalWrite(LED0, GPIO.HIGH)
	mcp.digitalWrite(LED1, GPIO.LOW)
	mcp.digitalWrite(LED2, GPIO.LOW)
	mcp.digitalWrite(LED3, GPIO.HIGH)
	while time.time()-startTime<4:
		mcp.digitalWrite(LED0,GPIO.LOW)
		mcp.digitalWrite(LED3,GPIO.LOW)
		mcp.digitalWrite(LED1,GPIO.HIGH)
		mcp.digitalWrite(LED2,GPIO.HIGH)
		time.sleep(1)
		mcp.digitalWrite(LED1,GPIO.LOW)
		mcp.digitalWrite(LED2,GPIO.LOW)
		mcp.digitalWrite(LED3,GPIO.HIGH)
		mcp.digitalWrite(LED0,GPIO.HIGH)
		time.sleep(1)
	

def patternTwo():
	startTime = time.time()
	while time.time()-startTime<4:
		for i in range(len(leds)):
			mcp.digitalWrite(leds[i], GPIO.LOW)
			time.sleep(0.5)
			mcp.digitalWrite(leds[i], GPIO.HIGH)
			time.sleep(0.5)
	
	
def patternThree():
	mcp.digitalWrite(LED0, GPIO.HIGH)
	mcp.digitalWrite(LED1, GPIO.HIGH)
	mcp.digitalWrite(LED2, GPIO.HIGH)
	mcp.digitalWrite(LED3, GPIO.HIGH)
	startTime = time.time()
	while time.time()-startTime<4:
		mcp.digitalWrite(LED0, GPIO.LOW)
		mcp.digitalWrite(LED1, GPIO.LOW)
		mcp.digitalWrite(LED2, GPIO.LOW)
		mcp.digitalWrite(LED3, GPIO.LOW)
		time.sleep(1)
		mcp.digitalWrite(LED0, GPIO.HIGH)
		mcp.digitalWrite(LED1, GPIO.HIGH)
		mcp.digitalWrite(LED2, GPIO.HIGH)
		mcp.digitalWrite(LED3, GPIO.HIGH)
		time.sleep(1)
	
	
def patternSwitch(pattern):
	patterns = [patternOne(), patternTwo(), patternThree()]
	newPattern = random.choice(patterns)
	
	while True:
		if newPattern == pattern:
			newPattern = random.choice(patterns)
		else:
			break
			
	return newPattern()


def partOne():
	list1 = [GPIO.HIGH, GPIO.LOW]
	while True:
		for i in list1:
			mcp.digitalWrite(LED0, i)
			time.sleep(2)
		
def partTwo():
	while True:
		for i in range(len(leds)):
			mcp.digitalWrite(leds[i], GPIO.LOW)
			time.sleep(0.5)
			mcp.digitalWrite(leds[i], GPIO.HIGH)
			#time.sleep(2)
			
def partThree():
	#mcp.portWrite(0)
	while True:
		if (mcp.digitalRead(SWITCH0) == GPIO.LOW):
			startTime = time.time()
			mcp.digitalWrite(LED0, GPIO.HIGH)
			mcp.digitalWrite(LED1, GPIO.LOW)
			mcp.digitalWrite(LED2, GPIO.LOW)
			mcp.digitalWrite(LED3, GPIO.HIGH)
			while time.time()-startTime<4:
				mcp.digitalWrite(LED0,GPIO.LOW)
				mcp.digitalWrite(LED3,GPIO.LOW)
				mcp.digitalWrite(LED1,GPIO.HIGH)
				mcp.digitalWrite(LED2,GPIO.HIGH)
				time.sleep(0.5)
				mcp.digitalWrite(LED1,GPIO.LOW)
				mcp.digitalWrite(LED2,GPIO.LOW)
				mcp.digitalWrite(LED3,GPIO.HIGH)
				mcp.digitalWrite(LED0,GPIO.HIGH)
				time.sleep(0.5)
			mcp.digitalWrite(SWITCH0, GPIO.HIGH)
			
			if (mcp.digitalRead(SWITCH0) == GPIO.LOW):
				#insert code here
				mcp.digitalWrite(SWITCH0,GPIO.HIGH)
				print "LET GO OF THE BUTTON PLS"
				time.sleep(0.5)
			else:
				mcp.digitalWrite(SWITCH0, GPIO.LOW)
			
		
		elif (mcp.digitalRead(SWITCH0) == GPIO.HIGH):
			startTime = time.time()
			mcp.digitalWrite(LED0, GPIO.HIGH)
			mcp.digitalWrite(LED1, GPIO.HIGH)
			mcp.digitalWrite(LED2, GPIO.HIGH)
			mcp.digitalWrite(LED3, GPIO.HIGH)
			startTime = time.time()
			while time.time()-startTime<4:
				mcp.digitalWrite(LED0, GPIO.LOW)
				mcp.digitalWrite(LED1, GPIO.LOW)
				mcp.digitalWrite(LED2, GPIO.LOW)
				mcp.digitalWrite(LED3, GPIO.LOW)
				time.sleep(0.5)
				mcp.digitalWrite(LED0, GPIO.HIGH)
				mcp.digitalWrite(LED1, GPIO.HIGH)
				mcp.digitalWrite(LED2, GPIO.HIGH)
				mcp.digitalWrite(LED3, GPIO.HIGH)
				time.sleep(0.5)
		
	
def main():
	#partOne()
	#partTwo()
	partThree()
main()

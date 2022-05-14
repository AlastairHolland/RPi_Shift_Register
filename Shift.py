import RPi.GPIO as GPIO

import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

outpins = [22, 23, 24]

relaynumber = 2

for i in outpins:
	GPIO.setup(i, GPIO.OUT)
	GPIO.output(i, GPIO.HIGH)
	
def Shift(output, relaynumber):
	for i in range(8*relaynumber):
		if output[i] == "1":
			GPIO.output(23, GPIO.LOW)
		elif output[i] == "0":
			GPIO.output(23, GPIO.HIGH)
		else:
			print("ERROR")
		GPIO.output(22, GPIO.HIGH)
		GPIO.output(22, GPIO.LOW)
	GPIO.output(24, GPIO.HIGH)
	GPIO.output(24, GPIO.LOW)
	
output = "00000000"*relaynumber
	
Shift(output, relaynumber)

def demo(relaynumber):
	connected = 12
	timer = 0.1
	while True:
		for i in range(connected):
			output = (i-1)*"0" + "1" + (8*relaynumber-i)*"0"
			Shift(output[::-1], relaynumber)
			time.sleep(timer)
		timer = timer - timer/10
	
def checkOutput(output, relaynumber):
	if output == "Demo":
		demo(relaynumber)
	if len(output)>8*relaynumber:
		print("Only " + str(8*relaynumber) + " bits will be displayed")
	elif len(output)<8*relaynumber:
		output = output + "0"*(8*relaynumber-len(output))
	return output[::-1]

def main(relaynumber):
	output = input("What output do you want? > ")
	output = checkOutput(output, relaynumber)
	Shift(output, relaynumber)
	main(relaynumber)
	

	
main(relaynumber)

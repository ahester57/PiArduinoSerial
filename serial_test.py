# Austin Hester 
# 11/11/17
# RPi3 Serial USB Communication

import serial
import time
import random

# It changes from ttyACM0 to ttyACM1, look for both
# Can we use regex here?
while True:
	time.sleep(0.1)
	try:
		ser = serial.Serial('/dev/ttyACM1', 9600, timeout=4)
		break
	except:
		try:
			ser = serial.Serial('/dev/ttyACM0', 9600, timeout=4)
			break
		except:
			pass

print "gotem"	# once connected
while True:
	time.sleep(0.2)
	try:
		r = random.randrange(0,2)
		if (r == 0):
			ser.write('4')
		else:
			ser.write('3')
	except:
		pass

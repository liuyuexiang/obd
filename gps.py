import serial

import string
import pynmea2
from datetime import datetime, timedelta

while True:
	port="/dev/ttyAMA0"
	ser=serial.Serial(port, baudrate=9600, timeout=0.5)
	dataout = pynmea2.NMEAStreamReader()
	newdata=ser.readline()

	if newdata[0:6] == "$GPRMC":
		newmsg=pynmea2.parse(newdata)
		
		lat=newmsg.latitude
		lng=newmsg.longitude
		dt = newmsg.timestamp
		print(dt.hour, dt.minute, dt.second)
		print((newmsg.datetime.utcnow() + timedelta(hours=8)).strftime("%m/%d/%Y, %H:%M:%S"))
        
		gps = "Latitude=" + str(lat) + " and Longitude=" + str(lng)
		print(gps)
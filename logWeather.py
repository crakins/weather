#!/usr/bin/env python

import os
import serial
import time, datetime
from sys import argv

def logWeather():

	while True:
		# get timestamp
		timestamp = time.localtime()
		year = timestamp[0]
		month = timestamp[1]
		day = timestamp[2]
		hour = timestamp[3]
		minute = timestamp[4]
		second = timestamp[5]
	
		# open serial connection and readline
		# weather format (temp, barotemp, humidity, pressure, altitude)
		connection = serial.Serial('/dev/ttyAMA0', 9600, timeout = 1)
		res = ""
		while res == "":
			res = connection.readline()
			# print(res) --error handeling
			
		if len(res) < 3:
			res = connection.readline()
				
		# calcualte time and append to weather data and remove '/r/n' 
		timestamp = time.asctime( time.localtime(time.time()) )
		weatherData = res.strip() + ',' + timestamp

		# open log.txt to append weather
		# if log.txt does not exist it will be created
		target = open('log.txt', 'a')
			
		# append line to log.txt
		target.write(weatherData + '\n')
		target.close()
		time.sleep(60)
	
if __name__ == "__main__":
	logWeather()

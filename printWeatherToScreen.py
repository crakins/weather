#!/usr/bin/env python

import os
import serial
import time 
from sys import argv

def readWeather():
	# read last line from log.txt
	logFile = open('log.txt', 'r')
	res = logFile.readlines()
	lastReading = res[-1]
	resList = []
	resList = lastReading.split(',')
	logFile.close()
	return(resList)

def convertToUS(metricList = []):
	englishList = []
	# c to f
	englishList.append(float(metricList[0]) * 1.8 + 32)
	englishList.append(float(metricList[1]) * 1.8 + 32)
	englishList.append(metricList[2])
	# Baro pressure
	englishList.append(metricList[3])
	# altitude, meters to feet
	englishList.append(float(metricList[4]) * 3.2808)
	# timestamp, no converstion
	englishList.append(metricList[5])
	return(englishList)

if __name__ == "__main__":
	
	# get last reading
	lastReadings = []
	lastReadings = readWeather()
	resList = convertToUS(lastReadings)
	
	# Write weather to screen
	print("Temperature: %s Fahrenheit" % resList[0])
	print("Barometer Temperature: %s Fahrenheit" % resList[1])
	print("Humidity: %s" % resList[2])
	print("Barometric Pressure: %s hPa" % resList[3])
	print("Altitude: %s Feet" % resList[4])
	print("Timestamp: %s" % resList[5])

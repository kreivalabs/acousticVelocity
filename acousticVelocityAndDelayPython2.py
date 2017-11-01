#!/usr/bin/env python

#version 1.1 / 31-October-2017

#prompt for user input
temp_fahrenheit = float(input("Enter temperture in degrees Fahrenheit: "))
measured_distance = float(input("Enter measured distance between speakers in feet: "))

#convert Fahrenheit to degrees Celsius
temp_celsius = (temp_fahrenheit - 32) / 1.8      

#calculate acoustic velocity in meters/second
meters_seconds = (temp_celsius * 0.6) + 331.4    

#convert meters/second to feet/millisecond
feet_milliseconds = meters_seconds * 0.00328084  

#calculate time differential based on acoustic velocity and measured distance
delay_time = measured_distance / feet_milliseconds

print"Approximate acoustic velocity is", meters_seconds, "m/s, or,", feet_milliseconds, "ft/ms."
print"Delay time is" , delay_time, "ms."
print"Press <Enter> to exit."
raw_input()

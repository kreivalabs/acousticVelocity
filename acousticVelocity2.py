#!/usr/bin/env python

temp_fahrenheit = float(input("Enter temperture in degrees Fahrenheit: "))
temp_celsius = (temp_fahrenheit - 32) / 1.8      
meters_seconds = (temp_celsius * 0.6) + 331.4    
feet_milliseconds = meters_seconds * 0.00328084  

print"Approximate acoustic velocity is", meters_seconds, "m/s, or,", feet_milliseconds, "ft/ms."
print"Press <Enter> to exit."
raw_input()

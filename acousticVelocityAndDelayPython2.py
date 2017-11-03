#!/usr/bin/env python

#version 1.3 / 02-November-2017

title="Acoustic Velocity and Loudspeaker Delay Calculator"
print title
print"=" * 80

# Prompt for user input
temp_fahrenheit = float(input("Enter temperture in degrees Fahrenheit: "))
measured_distance = float(input("Enter measured distance between speakers in feet: "))

# Convert Fahrenheit to degrees Celsius
temp_celsius = (temp_fahrenheit - 32) / 1.8      

# Calculate acoustic velocity in meters/second
meters_seconds = (temp_celsius * 0.6) + 331.4    

# Convert meters/second to feet/millisecond
feet_milliseconds = meters_seconds * 0.00328084  

# Calculate time differential based on acoustic velocity and measured distance
delay_time = measured_distance / feet_milliseconds

# Round results to two decimal places - suitable for most loudspeaker processing hardware and software
meters_seconds_round = str(round(meters_seconds, 2))
feet_milliseconds_round = str(round(feet_milliseconds, 2))
delay_time_round = str(round(delay_time, 2))

# Return results
print"=" * 80
print"Approximate acoustic velocity is:" 
print meters_seconds_round, "m/s, or", feet_milliseconds_round, "ft/ms." 
print""
print"Approximate delay time is" , delay_time_round, "ms."
print""
print"Press <Enter> to exit."
raw_input()

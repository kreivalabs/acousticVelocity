#!/usr/bin/env python

#version 1.2 / 01-November-2017

title='Acoustic Velocity and Loudspeaker Delay Calculator'
print(title)
print('=' * 80)

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

#return results
print('=' * 80)
print('Approximate acoustic velocity is:' 
print(meters_seconds, 'm/s, or,') 
print(feet_milliseconds, 'ft/ms.')
print()
print('Approximate delay time is', delay_time, 'ms.')
print()
print('Press <Enter> key to exit.')
input()

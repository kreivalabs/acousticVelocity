#!/usr/bin/env python

#versions 1.2 / 01-November-2017

#Calculate acoustic velocity in air based on temperature. Calculate resulting delay time
#in milliseconds for a measured distance. 
#NOTE: there is no method for factoring in gas density in air. Returned values are suitable
#for indoor use where temperature and humidity swings are not extreme.

#This script uses Future additions from http://www.python-future.org

#import Future additions
from __future__ import absolute_import, division, print_function, unicode_literals
from builtins import input

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

#display results
print('=' * 80)
print('Approximate acoustic velocity is:') 
print(meters_seconds, 'm/s, or,') 
print(feet_milliseconds, 'ft/ms.')
print()
print('Approximate delay time is', delay_time, 'm/s.')
print()
print('Press <Enter> to exit.')
input()

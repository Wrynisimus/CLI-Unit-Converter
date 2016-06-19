#!/usr/bin/python3
# imports all necessary modules for the program to function
import sys
import os
import argparse
import time

# define variables
def add(x, y):
	"""This adds two numbers together"""
	return x + y

def subtract(x, y):
	"""This subtracts two different numbers"""
	return x - y

def divide(x, y):
	"""This divides two different numbers"""
	return x / y

def multiply(x, y):
	"""This multiplies two different numbers"""
	return x * y

def square(x):
	"""This squares a number"""
	return x*x

def restart():
	"""Restarts the calculator"""
	python = sys.executable
	os.execl(python, python, * sys.argv)

# the program actually starts

print("Hello, I am a unit converter")
time.sleep(1)
print("Press 1 for Fahrenheit to Celsius")
time.sleep(.5)
print("Press 2 for Celsius to Fahrenheit")
time.sleep(.5)
print("Press 3 for Celsius to Kelvin")
time.sleep(.5)
print("Press 4 for Kelvin to Celsius")
time.sleep(.5)
print("Press 5 for Pounds to Kilograms")
time.sleep(.5)
print("Press 6 for Kilograms to Pounds")
choice = input("Choose (1/2/3/4/5/or 6) ")

# functions for converter to use

if choice == '1':
    num1 = float(input("Enter degrees Fahrenheit to convert to Celsius:"))
elif choice == '2':
    num1 = float(input("Enter degrees Celsius to convert to Fahrenheit:"))
elif choice == '3':
    num1 = float(input("Enter degrees Celsius to convert to Kelvin:"))
elif choice == '4':
    num1 = float(input("Enter degrees Kelvin to convert to Celsius:"))
elif choice == '5':
    num1 = float(input("Enter amount of Pounds to convert to Kilograms:"))
elif choice == '6':
    num1 = float(input("Enter amount of Kilograms to convert to Pounds:"))
else:
	print("That is not a correct command")


# Formulas used to convert this bullshit

if choice == '1':
    print("Your result is", (multiply( 5/9, subtract(num1, 32))), "°C")
if choice == '2':
    print("Your result is", add( 32, (multiply( 9/5, num1))), "°F")
if choice == '3':
    print("Your result is", add(num1, 273.15), "°K" )
if choice == '4':
    print("Your result is", subtract(num1, 273.15), "°C")
if choice =='5':
    print("Your result is", multiply(num1, .453), "Kg")
if choice =='6':
	print("Your result is", divide(num1, .453), "Pounds")

# the program begins the exit process

choice = input("Would you like to make another calculation (Yes) (No):")
if choice == 'Yes':
  restart()
if choice == 'yes':
  restart()
if choice == 'no':
  exec("raise SystemExit")
if choice == 'No':
  exec("raise SystemExit")
else:
  print("That is not a (Yes) or (No) answer, exiting program...")
  time.sleep(1)
  exec("raise SystemExit")

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
print("Hello I am calulator's brother, 'Converter'" "I am still in Alpha")
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
print("And Press 6 for Kilograms to Pounds")
time.sleep(1.5)
print("Damn, that's alot to remember")
choice = input("Choose (1/2/3/4/5/or 6) ")
# functions only for converter to use
if choice == '1':
    num1 = int(input("Enter degrees Fahrenheit to convert to Celsius:"))
if choice == '2':
    num1 = int(input("Enter degrees Celsius to convert to Fahrenheit:"))
if choice == '3':
    num1 = int(input("Enter degrees Celsius to convert to Kelvin:"))
if choice == '4':
    num1 = int(input("Enter degrees Kelvin to convert to Celsius:"))
if choice == '5':
    num1 = int(input("Enter amount of Pounds to convert to Kilograms:"))
if choice == '6':
    num1 = int(input("Enter amount of Kilograms to convert to Pounds:"))
# Formulas used to convert this bullshit
if choice == '1':
    print("Your result is...")
    print((multiply( 5/9, subtract(num1, 32))))
if choice == '2':
    print("Your result is...")
    print(add( 32, (multiply( 9/5, num1))))
if choice == '3':
    print("Your result is...")
    print(add(num1, 273.15))
if choice == '4':
    print("Your result is...")
    print(subtract(num1, 273.15))
if choice =='5':
    print("Your result is...")
    print(multiply(num1, .453))
if choice =='6':
    print("Your result is...")
    print(divide(num1, .453))

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
  exec("raise SystemExit")

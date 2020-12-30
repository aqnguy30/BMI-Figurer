#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 14:24:49 2020

@author: anhnguyen
"""

#Define class myException_1
class myException_1(Exception):
    pass

#Define function get_input()
def get_input():
    while True:
        try:
            h = float(input("Enter a positive height (in inches): "))
            w = float(input("Enter a positive weight (in pounds): "))
            if h < 0 or w < 0: #check if inputs are negative
                raise myException_1("something happened")
            return h, w
            break
        except ValueError: #check if inputs are not numbers
            print("Please enter only numbers. Try again!")
        except myException_1:
                print("Inputs should be positive, no negative. Try again!")
h, w = get_input()

#Define function calculate_BMI:
def calculate_BMI(h, w):
    BMI = w*703/(h**2) #formula calculate BMI
    return BMI
BMI = calculate_BMI(h, w)

#Define function calculate_weight_category:
def calculate_weight_category(BMI):
     #check conditions of BMI to fall into each weight category
    if BMI > 25:
        category = 'overweight'
    elif 18.5 <= BMI <= 25: 
        category = 'optimal weight'
    elif BMI < 18.5:
        category = 'underweight'
    #Display the output
    print("The person's BMI is", format(BMI, '.2f'), "which is", category)
calculate_weight_category(BMI)

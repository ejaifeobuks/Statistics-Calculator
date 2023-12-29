# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 15:17:09 2023

@author: OgheneobukomeEjaife
"""
import re
import statistics
import numpy as np
calculation=""    
class stat_tools:
    global calculation
    def __init__(self,calculation):
        self.calculation=calculation
        self.numbers=[float(num) for num in re.findall(r'-?\d+\.?\d*', self.calculation)]
    def calculate_statistic(self,func):
        return func(self.numbers) if self.numbers else f"No valid numbers for {func.__name__} calculation"
        
   
stat_calculator=stat_tools(calculation)

def add_to_calculation(symbol,text_result):
   global calculation
   calculation+=str(symbol)
   text_result.delete(1.0,"end")
   text_result.insert(1.0,calculation)
   stat_calculator.numbers = [float(num) for num in re.findall(r'-?\d+\.?\d*', calculation)]
def X_values(text_result):  
    global calculation
    global X_value
    X_value = [float(num) for num in re.findall(r'-?\d+\.?\d*', calculation)]
    text_result.delete(1.0,"end")
    text_result.insert(1.0,X_value)
    
def Y_values(text_result):  
    global calculation
    global Y_value
    Y_value = [float(num) for num in re.findall(r'-?\d+\.?\d*', calculation)]
    text_result.delete(1.0,"end")
    text_result.insert(1.0,Y_value)

def mean(text_result):
        mean_value =stat_calculator.calculate_statistic(statistics.mean)
        text_result.delete(1.0, "end")
        text_result.insert(1.0, mean_value)
def mode(text_result):
        mode_value = stat_calculator.calculate_statistic(statistics.mode)
        text_result.delete(1.0, "end")
        text_result.insert(1.0, mode_value)
    
def  Range(text_result):
         Range_value = max(stat_calculator.numbers)-min(stat_calculator.numbers)
         text_result.delete(1.0, "end")
         text_result.insert(1.0, Range_value)
def median(text_result):
         Median_value=stat_calculator.calculate_statistic(statistics.median)
         text_result.delete(1.0, "end")
         text_result.insert(1.0, Median_value)
def Standard_deviation(text_result):
        Standard_deviation_value=stat_calculator.calculate_statistic(statistics.pstdev)
        text_result.delete(1.0, "end")
        text_result.insert(1.0, Standard_deviation_value)
def Variance(text_result):
        Variance_value=stat_calculator.calculate_statistic(statistics.pvariance)
        text_result.delete(1.0, "end")
        text_result.insert(1.0, f"Variance({calculation})\n {Variance_value}")
        
def Coefficient_of_Variation(text_result):
    global calculation
    numbers = [float(num) for num in re.findall(r'-?\d+\.?\d*', calculation)]

    # Check if there are numbers to calculate the mean
    if numbers:
        CV=(np.std(numbers,ddof=0)/np.mean(numbers))*100
        text_result.delete(1.0, "end")
        text_result.insert(1.0, CV)
    else:
        text_result.delete(1.0, "end")
        text_result.insert(1.0, "No valid numbers for Coefficient of Variation calculation")
def Regression(text_result):
    global X_value
    global Y_value
    slope,intercept=statistics.linear_regression(X_value,Y_value)
    regression_details=f"Slope:{slope},Intercept:{intercept}"
    text_result.delete(1.0, "end")
    text_result.insert(1.0, regression_details)
    
def clear_field(text_result):
        global calculation
        calculation=""
        stat_calculator.numbers = []  # Reset the list of numbers
        text_result.delete(1.0,"end")
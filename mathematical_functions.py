# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 15:17:09 2023

@author: [Your Name]
"""
import re
import statistics
import numpy as np

class StatTools:
    def __init__(self):
        self.expression = ""
        self.numbers = []

    def add_to_expression(self, symbol):
        self.expression += str(symbol)
        self._update_numbers()

    def _update_numbers(self):
        self.numbers = [float(num) for num in re.findall(r'-?\d+\.?\d*', self.expression)]

    def clear_expression(self):
        self.expression = ""
        self.numbers = []

    def calculate_statistic(self, func):
        if self.numbers:
            try:
                return func(self.numbers)
            except statistics.StatisticsError as e:
                return f"Error: {e}"
        else:
            return f"No valid numbers for {func.__name__} calculation"

    def get_values(self):
        return self.numbers

# Create an instance of StatTools
stat_calculator = StatTools()

# Functions interacting with the StatTools instance
def add_to_calculation(symbol, text_result):
    stat_calculator.add_to_expression(symbol)
    text_result.delete("1.0", "end")
    text_result.insert("1.0", stat_calculator.expression)

def get_values(text_result):
    values = stat_calculator.get_values()
    text_result.delete("1.0", "end")
    text_result.insert("1.0", values)

def mean(text_result):
    mean_value = stat_calculator.calculate_statistic(statistics.mean)
    text_result.delete("1.0", "end")
    text_result.insert("1.0", mean_value)

def mode(text_result):
    mode_value = stat_calculator.calculate_statistic(statistics.mode)
    text_result.delete("1.0", "end")
    text_result.insert("1.0", mode_value)

def data_range(text_result):
    if stat_calculator.numbers:
        range_value = max(stat_calculator.numbers) - min(stat_calculator.numbers)
        text_result.delete("1.0", "end")
        text_result.insert("1.0", range_value)
    else:
        text_result.delete("1.0", "end")
        text_result.insert("1.0", "No valid numbers for range calculation")

def median(text_result):
    median_value = stat_calculator.calculate_statistic(statistics.median)
    text_result.delete("1.0", "end")
    text_result.insert("1.0", median_value)

def standard_deviation(text_result):
    std_dev_value = stat_calculator.calculate_statistic(statistics.pstdev)
    text_result.delete("1.0", "end")
    text_result.insert("1.0", std_dev_value)

def variance(text_result):
    variance_value = stat_calculator.calculate_statistic(statistics.pvariance)
    text_result.delete("1.0", "end")
    text_result.insert("1.0", variance_value)

def coefficient_of_variation(text_result):
    if stat_calculator.numbers:
        mean_value = statistics.mean(stat_calculator.numbers)
        if mean_value != 0:
            cv = (statistics.pstdev(stat_calculator.numbers) / mean_value) * 100
            text_result.delete("1.0", "end")
            text_result.insert("1.0", cv)
        else:
            text_result.delete("1.0", "end")
            text_result.insert("1.0", "Mean is zero, cannot calculate Coefficient of Variation")
    else:
        text_result.delete("1.0", "end")
        text_result.insert("1.0", "No valid numbers for Coefficient of Variation calculation")

def regression(text_result, x_values, y_values):
    try:
        slope, intercept = statistics.linear_regression(x_values, y_values)
        regression_details = f"Slope: {slope}, Intercept: {intercept}"
        text_result.delete("1.0", "end")
        text_result.insert("1.0", regression_details)
    except Exception as e:
        text_result.delete("1.0", "end")
        text_result.insert("1.0", f"Error: {e}")

def clear_field(text_result):
    stat_calculator.clear_expression()
    text_result.delete("1.0", "end")

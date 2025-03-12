import numpy as np
import math
import tkinter as tk

def log_with_base(base, number):
    return math.log(number) / math.log(base)

def calculate_and_print_2dec(calc):
    print("{:.2f}".format(calc))

def calculate_and_print_floor(calc):
    print(int(calc))

def calculate_and_print_ceil(calc):
    print(math.ceil(calc))

# Define functions mapping
calc_functions = {
    1: calculate_and_print_2dec,
    2: calculate_and_print_floor,
    3: calculate_and_print_ceil
}

# Ask user for choice
print("Enter the calculation:")
string_calc = input()
calc = eval(string_calc)

print("Choose the operation:")
print("1. Calculate and print as 2 decimals")
print("2. Calculate and print as floor")
print("3. Calculate and print as ceil")
choice = int(input("Enter your choice (1/2/3): "))


# Check if choice is valid
if choice in calc_functions:
    print("THE RESULT IS:")
    calc_functions[choice](calc)
else:
    print("Invalid choice")

# === CS 115 Lab 3 ===
# Fill in your name and the Stevens Honor Code pledge on the following lines.
# Failure to fill this in will result in deducted marks.
#
# Name:Jake Talvy
#
# Pledge:I pledge my honor that I have abided by the Stevens Honor System.
#
from functools import reduce
# === CS 115 Lab 3 ===
#
# You are welcome and encouraged to define additional functions here.
# ---

# ---

def add(x,y):
    """returns the sum of two numbers"""
    return x+y

def is_none(data):
    """returns a bool value as to whether or not the data is None returns false if
    None so the filter knows to remove it"""
    if data == None:
        return False
    else:
        return True
    
def square(number):
    """returns the number squared"""
    return number ** 2

def reciprocal(number):
    """returns the reciprocal of a number"""
    return 1/number

def mean(data):
    """returns the average of the numbers in the inputted tuple"""
    total = reduce(add, data)
    length = len(data)
    return total/length

def rms(data):
    """filters the data and returns the root mean square of the numbers in data"""
    filtered_numbers = filter(is_none, data)
    squared_numbers = list(map(square, filtered_numbers))
    squared_average = mean(squared_numbers)
    return squared_average ** 0.5

def hm(data):
    """filters the data and returns the harmonic mean of the numbers in data"""
    filtered_numbers = filter(is_none, data)
    reciprocals = list(map(reciprocal,filtered_numbers))
    reciprocals_avg = mean(reciprocals)
    return reciprocal(reciprocals_avg)



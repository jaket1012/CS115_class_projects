# === CS 115 Lab 4 ===
# Fill in your name and the Stevens Honor Code pledge on the following lines.
# Failure to fill this in will result in deducted marks.
#
# Name:Jake Talvy
#
# Pledge:I pledge my honor that I have abided by the Stevens Honor System.
#
# === CS 115 Lab 4 ===
def factorial(n):
    """returns the factorial of the given number n"""
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)

def power_seq(a, n):
    """returns a tuple of a to every power from 0 to n"""
    if n == 0:
        return tuple([1])
    else:
        return power_seq(a, n-1) + tuple([a**n])

def my_len(tup):
    """returns the length of the tuple"""
    if tup == ():
        return 0
    if tup == tup[0]:
        return 1
    else:
        return 1 + my_len(tup[1:])

def dot(xs, ys):
    """returns the dot product of the two inputted tuples"""
    if my_len(xs) == 0 or my_len(ys) == 0:
        return 0
    if my_len(xs) == 1 or my_len(ys) == 1:
        return xs[0]*ys[0]
    else:
        return xs[0]*ys[0] + dot(xs[1:], ys[1:])

def poly(coeffs, x):
    """evaluates a polynomial given the coeffecients and the x value"""
    powers = power_seq(x, my_len(coeffs))
    return dot(coeffs, powers)


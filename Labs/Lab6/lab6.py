# === CS 115 Lab 6 ===
# Fill in your name and the Stevens Honor Code pledge on the following lines.
# Failure to fill this in will result in deducted marks.
#
# Name:Jake Talvy
#
# Pledge:I pledge my honor that I have abided by the Stevens Honor System.
#
# === CS 115 Lab 6 ===
def to_int(tup, base):
    """takes in a tuple representing a number in the inputted base and converts it to a number in base 10"""
    if len(tup) == 0:
        return 0
    return tup[0]*(base**(len(tup)-1)) + to_int(tup[1:], base)

def to_base(n, base):
    """takes in a number from base 10 and converts it into a new number in the inputted base"""
    if n == 0:
        return ()
    if n < base:
        return tuple([int(n)])
    num = n/base
    remainder = n%base
    return to_base(num, base) + tuple([int(remainder)])


# === CS 115 Lab 01 ===
# Fill in your name and the Stevens Honor Code pledge on the following lines.
# Failure to fill this in will result in deducted marks.
#
# Name:Jake Talvy
#
# Pledge:I pledge my honor that I have abided by the Stevens Honor System.
#
# === CS 115 Lab 01 ===
def consecutive_sum(x, y):
    """
    Takes 2 number inputs and returns the sum of all numbers between x and y.
    """
    return (y+x-1)/2 * (y-x)

def same_ends(word):
    """
    Takes a word and checks if the words first letter is the same as its last letter.
    """
    if word[0] == word[-1]:
        return True
    return False

def is_palindromic(word):
    """
    Takes an imput word and determines whether or not it is a palindrome
    """
    reverse = word[::-1]
    if word.lower() == reverse.lower():
        return True
    else:
        return False

def get_ticket_price(age):
    """
    Takes an input age and returns the ticket price based on the age
    under 3 is $0
    between 3 and 12 is $10
    between 13 and 64 is $15
    65 and older is $12
    """
    if age < 3:
        return 0
    elif age >= 3 and age <=12:
        return 10
    elif age >= 13 and age <=64:
        return 15
    elif age >= 65:
        return 12


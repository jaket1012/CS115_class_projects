# === CS 115 Homework 2 ===
# Fill in your name and the Stevens Honor Code pledge on the following lines.
# Failure to fill this in will result in deducted marks.
#
# Name:Jake Talvy
#
# Pledge:I pledge my honor that I have abided by the Stevens Honor System.
#
# === CS 115 Homework 2 ===
import sys
sys.setrecursionlimit(10000) # Allows up to 10000 recursive calls
from functools import reduce
morse = (
    ('.-', 'A'), ('-...', 'B'), ('-.-.', 'C'), ('-..', 'D'), ('.', 'E'),
    ('..-.', 'F'), ('--.', 'G'), ('....', 'H'), ('..', 'I'), ('.---', 'J'),
    ('-.-', 'K'), ('.-..', 'L'), ('--', 'M'), ('-.', 'N'), ('---', 'O'),
    ('.--.', 'P'), ('--.-', 'Q'), ('.-.', 'R'), ('...', 'S'), ('-', 'T'),
    ('..-', 'U'), ('...-', 'V'), ('.--', 'W'), ('-..-', 'X'), ('-.--', 'Y'),
    ('--..', 'Z')
)

#dictionary = ("AM", "AS", "BE", "BED", "CAN", "EGG", "HE", "HER", "HIM",
#    "HIS", "ILL", "IS", "KID", "ME", "MY", "ON", "OR", "SEE", "SO", "TO",
#    "TOE", "TOW", "WAS", "WOW",)


# Uncomment one of the following lines to try your code
# with a larger dictionary of words:
from dict import dictionary
#from bigdict import dictionary

def find_morse(text, morse_translation):
    """goes through a tuple of letters and morse code and returns the morse code
    equivalent of the inputted letter"""
    if text == morse_translation[0][1]:
        code = morse_translation[0][0]
        return code
    else:
        return find_morse(text, morse_translation[1:])

def find_letter(text, morse_translation):
    """goes through a tuple of morse code and letters and returns the letter
    equivalent of the inputted morse code"""
    if text == morse_translation[0][0]:
        code = morse_translation[0][1]
        return code
    elif len(morse_translation) > 1:
        return find_letter(text, morse_translation[1:])
    else:
        return "?"

def does_match(text, word):
    """returns true if the inputted morse code without spaces matches
    the inputted word"""
    morse_word_split = encode(word).split(" ")
    morse_word = reduce(lambda x,y: x+y, morse_word_split)
    if text == morse_word:
        return True
    else:
        return False

def find_matches(text, dictionary):
    """goes through the dictionary and returns a list of all the words that
    could match the inputted morse code without spaces"""
    if len(dictionary) == 1:
        if text == dictionary[0]:
            return dictionary[0]
        else:
            return []
    elif does_match(text, dictionary[0]):
        return [dictionary[0]] + find_matches(text, dictionary[1:])
    else:
        return find_matches(text,dictionary[1:])

def combine_strings(x, y):
    """combines two strings into one"""
    new_string = x + y
    return new_string

def encode(plaintext):
    """encodes the inputted word into morse code with spaces in between
    each translated letter"""
    letter = plaintext[0]
    encoded_letter = find_morse(letter, morse)
    if len(plaintext) == 1:
        return encoded_letter
    else:
        return encoded_letter + " " + encode(plaintext[1:])
    
def decode(cyphertext):
    """decodes the inputted morse code into an all uppercase word
    if some of the morse code doesnt match any real morse code it
    will put a ? into the word"""
    to_decode = cyphertext.split(" ")
    decoded_message = list(map(lambda x: find_letter(x,morse), to_decode))
    one_message = reduce(combine_strings, decoded_message)
    return one_message

def matches(cyphertext):
    """returns a list of all the words that could match the
    inputted morse code without spaces"""
    return find_matches(cyphertext, dictionary)





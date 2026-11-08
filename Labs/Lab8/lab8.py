# === CS 115 Lab 8 ===
# Fill in your name and the Stevens Honor Code pledge on the following lines.
# Failure to fill this in will result in deducted marks.
#
# Name:Jake Talvy
#
# Pledge:I pledge my honor that I have abided by the Stevens Honor System.
#
# === CS 115 Lab 8 ===
def times_one(L):
    """maps x*1 onto a list"""
    return list(map(lambda x: x*1, L))

def copy_3d(lll):
    """makes a deep copy of the inputted list"""
    return list(map(times_one, lll))


def check_copy_3d(lll_1, lll_2):
    """checks in copy_3d made a deep copy"""
    x = copy_3d(lll_1)
    y = lll_1[0][0]
    x[0][0] = 999
    if lll_1 == lll_2 and not lll_1[0] is lll_2[0] and not x[0][0] == lll_1[0][0]:
        return True
    lll_1[0][0] = y
    return False


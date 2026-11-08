# === CS 115 Lab 2 ===
# Fill in your name and the Stevens Honor Code pledge on the following lines.
# Failure to fill this in will result in deducted marks.
#
# Name:Jake Talvy
#
# Pledge:I pledge my honor that I have abided by the Stevens Honor System.
#
# === CS 115 Lab 2 ===
import re

def vali_date_impl_1(month, day):
    """
    Given a month as an integer and day as an integer,
    returns whether that month and day correspond to a
    valid date on a standard Gregorian calendar,
    including on leap years.
    """
    return day - month % 2 < 30

def vali_date_impl_2(month, day):
    """
    Given a month as an integer and day as an integer,
    returns whether that month and day correspond to a
    valid date on a standard Gregorian calendar,
    including on leap years.
    """
    month_map = ["voi",
                 "jan",
                 "feb",
                 "mar",
                 "apr",
                 "may",
                 "jun",
                 "jul",
                 "aug",
                 "sep",
                 "oct",
                 "nov",
                 "dec",]
    try:
        m = month_map[month]
    except IndexError:
        m = "ind"
    s = "{}{:>02d}".format(m, day)
    regex = re.compile(r"([sn].*|.un|a.r)([012].|30)|(..b[^3456789].)|(j(a.|.l)|[mod].*|a.g)([012].|3[01])")
    return regex.fullmatch(s) is not None

def vali_date_impl_3(month, day):
    """
    Given a month as an integer and day as an integer,
    returns whether that month and day correspond to a
    valid date on a standard Gregorian calendar,
    including on leap years.
    """
    return (day - 0 ** abs((month-1) % 12 - (month-1))) == (day-1) % (30 + 0 ** ((month-1) % 7 % 2) - 0 ** ((month+10) % 30 % 12))

def vali_date_impl_4(month, day):
    """
    Given a month as an integer and day as an integer,
    returns whether that month and day correspond to a
    valid date on a standard Gregorian calendar,
    including on leap years.
    """
    return False

def vali_date_impl_5(month, day):
    """
    Given a month as an integer and day as an integer,
    returns whether that month and day correspond to a
    valid date on a standard Gregorian calendar,
    including on leap years.
    """
    return month == 1 or month == 2 or month == 3 or month == 4 or \
            month == 5 or month == 6 or month == 7 or month == 8 or \
            month == 9 or month == 10 or month == 11 or month == 12 and \
            day == 1 or day == 2 or day == 3 or day == 4 or day == 5 or \
            day == 6 or day == 7 or day == 8 or day == 9 or day == 10 or \
            day == 11 or day == 12 or day == 13 or day == 14 or day == 15 or \
            day == 16 or day == 17 or day == 18 or day == 19 or day == 20 or \
            day == 21 or day == 22 or day == 23 or day == 24 or day == 25 or \
            day == 26 or day == 27 or day == 28 or day == 29 or day == 30 or \
            day == 31 and \
            not (day == 31 and month == 2 or month == 4 or month == 6 or \
                            month == 9 or month == 11) and \
            not (day > 29 and month == 2)

def vali_date_buggy_but_fixable(month, day):
    """
    Given a month as an integer and day as an integer,
    returns whether that month and day correspond to a
    valid date on a standard Gregorian calendar,
    including on leap years.
    """
    if month < 1 or month > 12:
        return False
    if day < 1:
        return False
    if month in (4, 6, 9, 11):
        return day <= 30
    if month == 2:
        return day <= 29
    return day <= 31

# Change the line below to switch which implementation your code is testing.
vali_date = vali_date_impl_4


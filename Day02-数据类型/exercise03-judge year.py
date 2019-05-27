"""
input a year and judge if it is
a leap year...if return True
else return False

"""

try:
    year = int(input('Please input a year: '))
    if len(str(year)) != 4:
        raise ValueError
except ValueError:
    print('Please input a year...')
else:
    # leap year is a year can be divided by 4 or 400 but not 100
    is_leap = (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
    print(is_leap)
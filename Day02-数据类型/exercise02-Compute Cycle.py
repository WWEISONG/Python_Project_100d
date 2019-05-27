"""
input radius
and then compute perimeter and area

"""

import math, sys

try:
    radius = float(input('Please input the radius: '))
except ValueError:
    print('Please input a number...')
    sys.exit()
else:
    perimeter = 2 * math.pi * radius
    area = math.pi * radius ** 2
    print(f'perimeter: {perimeter:.2f}')
    print(f'area: {area:.2f}')
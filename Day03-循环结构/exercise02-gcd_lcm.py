x = int(input('x = '))
y = int(input('y = '))
if x > y:
    x, y = y, x
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print(f'{x} and {y}\'s gcd is {factor}.')
        print(f'{x} and {y}\'s lcm is {abs(x * y) // factor}')
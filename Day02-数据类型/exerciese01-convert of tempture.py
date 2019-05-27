"""
convert Fahrenheit to Centigrade

Atuther: SONGWEI
"""
try:
    F = float(input('Please input Fahrenheit: '))
except ValueError:
    print('Please input a number...')
else:
    C = (F - 32) / 1.8
    print(f'{F:.1f} = {C:.1f} Centigrade')
'''
--- July 22nd, 2016
Script to calculate the binominal efficiency from two values asked to the user
'''

import math
from uncertainties import ufloat

def askForValues():
    input_numerator = raw_input('what is your numerator?: ')
    input_denominator = raw_input('what is your denominator?: ')
    if float(input_numerator) > float(input_denominator):
        print 'The numerator can\'t be higher than the denominator! Try again! '
        del input_numerator, input_denominator
        input_numerator, input_denominator = askForValues()
    return input_numerator, input_denominator

def calculateEfficiency(num, den):
    if num < den:
        eff = num/den
        err = 1/den * math.sqrt(num * (1-eff))
    elif num == den:
        eff = 1.0
        err = 1.0
    return eff, err

x, y = askForValues()
efficiency, error = calculateEfficiency(float(x), float(y))
tot_eff = ufloat(efficiency, error)

print 'The efficiency is', tot_eff

import math
import stdio


while True:
    x = float(input('This is homework from Abdullah Nil \n Please input any number for take square root: '))
    if x < 0:
        stdio.writeln('You should not use the negative numbers')
        stdio.writeln('Please try again with a positive number')

    else:
        stdio.writeln('Taking the square root of the given expression...')
        stdio.writeln(math.sqrt(x))
        break
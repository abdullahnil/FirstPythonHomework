import math


while True:
    x = float(input('This is homework from Abdullah Nil \n Please input any number for take square root: '))
    if x < 0:
        print('You should not use the negative numbers')
        print('Please try again with a positive number')

    else:
        print('Taking the square root of the given expression...')
        print(math.sqrt(x))
        break

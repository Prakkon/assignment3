from math import *

def task2():
    x = int(input("Enter a number: "))
    if x > 0:
        output1 = sqrt(x)
        output2 = log(x, e)
        output3 = sin(x)
        print("Square root: ", output1, "\nLogarithm: ", output2, "\nSine: ", output3)

    else:
        print("Please enter a number greater than 0")
    return

task2()
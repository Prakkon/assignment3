
def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)

def task1():
    x = int(input("Enter a number: "))
    output = factorial(x)
    print("Factorial of " + str(x) + " is: " + str(output))
    return


task1()



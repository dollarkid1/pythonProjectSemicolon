from GCDFunction import *


def test_gcd_f():
    print("GREATEST COMMON DIVISOR")
    num1 = eval(input("enter a number:\n"))
    num2 = eval(input("enter a number:\n"))
    print("The GCD for " + str(num1) + " and " + str(num2) + " are: ")
    print(gcd_f(num1, num2))


test_gcd_f()



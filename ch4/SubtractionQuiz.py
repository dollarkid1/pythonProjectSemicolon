import random

number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

if number2 > number1:
    number1, number2 = number2, number1

answer = eval(input("What is " + str(number1) + " - " + str(number2) + "?\n"))
if answer == number1 - number2:
    print("Correct")
else:
    print("wrong")

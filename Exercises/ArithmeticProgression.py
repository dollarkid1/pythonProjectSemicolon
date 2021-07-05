def ap():
    num1, num2, num3 = eval(input("Enter Numbers separated by commas"))
    if num2 - num1 == num3 - num2:
        ver = num3 - num2
        print(num1, num2, num3, ver + num3)


ap()

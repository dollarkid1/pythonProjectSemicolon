def gcd_f(number1=10, number2=250):
    gcd = 1
    k = 2
    while k <= number1 and k <= number2:
        if number1 % k == 0 and number2 % k == 0:
            gcd = k
        k += 1
    return gcd


print(gcd_f(number1=100))


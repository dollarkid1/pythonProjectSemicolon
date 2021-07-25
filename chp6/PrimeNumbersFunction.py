def is_prime(x):
    div = 2
    t = True
    while div <= x / 2:
        if x % div:
            t = False
        div += 1
    print(t)



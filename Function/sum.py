def m(i1, i2):
    result = 0
    for i in range(i1, i2 + 1):
        result += i
    return result


def main():
    print("Sum from 1 to 10 is ", m(1, 10))
    print("Sum from 39 to 190 is ", m(39, 190))
    print("Sum from 139 to 1830 is ", m(139, 1830))


main()
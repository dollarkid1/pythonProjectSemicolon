def analyzer():
    passes = 0
    failures = 0
    print("enter results (pass = 1 and fail = 2)\n")
    for i in range(10):
        result = int(input())
        if result == 1:
            passes += 1
        else:
            failures += 1

    print(f'Students Passed = {passes}')
    print(f'Students Failed = {failures}')

    if passes > 8:
        print("Bonus to the Instructor")


analyzer()

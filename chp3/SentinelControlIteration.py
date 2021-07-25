def average():
    total = 0
    grade_counter = 0

    grade = int(input("Enter grade, and -1 to exit\n"))

    while grade != -1:
        total += grade
        grade_counter += 1
        grade = int(input("Enter grade, and -1 to exit\n"))

    if grade_counter != 0:
        print(f'the grades average is {total / grade_counter :.2f}')

    else:
        print("No grade entered!")


average()

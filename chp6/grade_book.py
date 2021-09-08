grade_book = {
    'Dan': [50, 40, 59],
    'Susan': [49, 23, 52],
    "Fred": [94, 48, 82]
}

all_grades_total = 0
all_grades_count = 0

for name, grades in grade_book.items():
    total = sum(grades)
    print(f'Average for {name} is {total/len(grades):.2f}')
    all_grades_total += sum(total)
    all_grades_count += len(grades)
print(f"Class's average is: {all_grades_total / all_grades_count:.2f}")

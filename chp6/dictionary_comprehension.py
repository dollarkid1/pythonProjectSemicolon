month1 = {'January': 1, 'February': 2, 'March': 3}
print(month1)
print()
month2 = {number: name for name, number in month1.items()}
print(month2)
print()
grades = {'Sue': [98, 87, 94], 'Bob': [84, 95, 91]}
grades2 = {z: sum(x) / len(x) for z, x in grades.items()}
print(grades2)

a = {number: number ** 3 for number in range(1, 6)}
print(a, end=' ')


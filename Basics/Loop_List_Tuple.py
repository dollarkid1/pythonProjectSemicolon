# Appending to a List with +=
a_list = []
for numbers in range(1, 11):
    a_list += [numbers]
print(f'a_list = {a_list}')

letters = []
letters += 'python'
print(letters)

# Concatenating Lists with +

list1 = [10, 20, 30]
list2 = [40, 50]
concatenated_list = list1 + list2
print(concatenated_list)

# Using for and range to Access List Indices and Values

for i in range(len(concatenated_list)):
    print(f'{i}: {concatenated_list[i]}')

# Comparison Operators

a = [1, 2, 3]
b = [1, 2, 3]
c = [1, 2, 3, 4]
print(a == b)
print(c == a)
print(c >= b)


def cube_list(values):
    for e in range(len(values)):
        values[e] **= 3
        d = values
    print(d)


numbers = [1, 2, 3, 4, 5]
cube_list(numbers)

# Appending Tuples to Lists

num = [100, 200, 300]
num += 400, 500
print(num)

# Tuples May Contain Mutable Objects

student_info = ("Fata", "Fred", [1, 2, 4])
student_info[2][2] = 3
print(student_info)
r, t, y, u, o = range(1, 10, 2)
print(r, t, y, u, o)

color = ["red", "orange", "blue", "white", "pink"]

# Inserting an Element at a Specific List Index
color.insert(1, "brown")
print(color)
# Adding an Element to the End of a List
color.append("black")
print(color)
e = ['grey', "violet"]
color.extend(e)
print(color)
color.remove('black')
color.count("black")
print(color.pop(2))
color.reverse()
print(color)
color.pop(0)
print(color)
list4 = list(range(1, 11))
list0 = [i for i in list4 if i % 2 == 0]
print(list0)
colors = ['red', 'orange', 'yellow', 'green', 'blue']
color2 = [t.upper() for t in colors]
print(color2)
print(colors)
cube = [(x, x ** 3) for x in range(1, 6)]
print(cube)
multiples = [x for x in range(3, 30, 3)]
print(multiples)

import random

list1 = []
for i in range(1, 11):
    list1.append(random.randint(1, 99))
print(list1)
for i in (x ** 2 for x in list1 if x % 2 != 0):
    print(i, end='-' + str(random.randint(1, 99)))

items = [1, 2, 3, 4, 5]

list3 = [item ** 2 for item in items]
print(list3)

items = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]


def checker(param):
    data = []
    for x in param:
        x = x ** 2
        if x % 2 != 0:
            data.append(x)
    return data


for value in checker(items):
    print(value, end="  ")

#

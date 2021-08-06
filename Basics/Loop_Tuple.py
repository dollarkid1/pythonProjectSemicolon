fruits = ["Apple", "Orange", "Pear", "Guava", "Peach"]

a = list(enumerate(fruits))
b = tuple(enumerate(fruits))
print(a)
print(b)

for rating, choice in enumerate(fruits):
    print(f'{rating}: {choice}')
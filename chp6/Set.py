colors = {'red', 'orange', 'yellow', 'green', 'red', 'blue'}
print(colors)
print(len(colors))
print('pink' in colors)
print('red' in colors)
for color in colors:
    print(color.upper(), end=" ")
print()
num = list(range(11)) + list(range(5))
print(num)
a = set(num)
print(a)
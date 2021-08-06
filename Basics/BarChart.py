numbers = [14, 9, 21, 5, 17]
print("Printing BarChart through numbers")
print(f'Index {"Number" :>7}    Bar')
for index, number in enumerate(numbers):
    print(f'{index + 1 :>5}: {number :>5}  {"*" * number}')
print(numbers[-1::-1])
o = 8 in numbers
print(o)
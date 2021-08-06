numbers = [12, 43, 17, 83, 43]
a = numbers.index(43)
print(a)
if 44 in numbers:
    print(f'{44} found in index {numbers.index(44)}')
else:
    print(f'{44} not found')
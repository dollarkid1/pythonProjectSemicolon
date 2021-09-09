import random
from collections import Counter

number = [random.randrange(1, 11) for i in range(5)]

counts = Counter(number)

for value, count in sorted(counts.items()):
    print(f'{value:<4} {count}')

country_code = {}
country_code.update(Australia='Au', Nigeria='ng')
print(country_code)

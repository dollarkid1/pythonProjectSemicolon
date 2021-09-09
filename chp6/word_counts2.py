from collections import Counter

text = ('i am douglas humble a software engineer '
        'i love who i am and am douglas humble a software engineer')

counter = Counter(text.split())

for word, count in sorted(counter.items()):
    print(f'{word:<12}{count}')
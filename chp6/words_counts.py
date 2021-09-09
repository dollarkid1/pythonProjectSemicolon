text = ('i am douglas humble a software engineer '
        'i love who i   am and am douglas humble a software engineer')

word_count = {}

for word in text.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(f'{"WORD":<12}COUNT')

for word, count in sorted(word_count.items()):
    print(f'{word:<12}{count}')

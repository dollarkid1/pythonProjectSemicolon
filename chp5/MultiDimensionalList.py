a = [[3, 4, 53], [43, 4, 2], [3, 23, 6]]
for i in a:
    for m in i:
        print(m, end=" ")
        print()


for i, row in enumerate(a):
    for j, item in enumerate(row):
        print(f'a[{i}][{j}]={item} ', end=' ')
        print()
l = [64, 25, 12, 22, 11, 1, 2, 44, 3, 122, 23, 34]

for i in range(len(l)):
    for j in range(i + 1, len(l)):

        if l[i] > l[j]:
           l[i], l[j] = l[j], l[i]
evenList = []
oddList = []
for i in range(len(l)):
    if l[i] % 2 == 0:
        evenList.append(l[i])
    if l[i] % 2 == 1:
        oddList.append(l[i])

for i in oddList:
    evenList.append(i)

print(evenList)
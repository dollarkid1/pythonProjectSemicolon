numbers = [3, 2, 18, 0, 7, 6]

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):

        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

evenList = []
oddList = []

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        evenList.append(numbers[i])
    if numbers[i] % 2 == 1:
        oddList.append(numbers[i])

for i in oddList:
    evenList.append(i)

print(evenList)

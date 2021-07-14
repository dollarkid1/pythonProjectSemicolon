for i in range(1, 5):
    j = 0
    while j < i:
        print(j, end=" ")
        j += 1

print()
print("----------------------------------------")
i = 0
while i < 5:
    for j in range(i, 1, -1):
        print(j, end=" ")
    print("****")
    i += 1
print()
print("----------------------------------------")

i = 5
while i >= 1:
    num = 1
    for j in range(1, i + 1):
        print(num, end="xxx")
        num *= 2
print()
i -= 1

print()
print("----------------------------------------")

i = 1
while i <= 5:
    num = 1
    for j in range(1, i + 1):
        print(num, end="G")
        num += 2
print()
i += 1

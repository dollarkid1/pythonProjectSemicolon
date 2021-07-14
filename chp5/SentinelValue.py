
sum = 0
data = 0
while data != -1:
    data = eval(input("Enter the data you want to sum and -1 to get the result\n"))
    sum += data

print(sum)
number = 0
sum = 0
for count in range(5):
    number = eval(input("Enter an integer: "))
    sum += number
    print("sum is", sum)
    print("count is", count)

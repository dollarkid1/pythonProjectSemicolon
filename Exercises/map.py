fahrenheit = [41, 32, 212]
celsius = list[map(lambda x: (x, (x - 32) * 5/9), fahrenheit)]
print(celsius)
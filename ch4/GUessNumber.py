import random

guess = eval(input("Guess the number between 1 - 1000\n"))
number = random.randint(1, 1000)
count = 1
while guess != number:
    if guess < number:
        guess = eval(input("Too low. Try Again.\n"))
    else:
        guess = eval(input("Too high. Try Again.\n"))
    count += 1

    if count % 10 == 0:
        print("You should be able to do better!")

if guess == number:
    print("Congrats!. You guessed the number.")

    if count < 5:
        print("Either you know the secret or You got lucky!")

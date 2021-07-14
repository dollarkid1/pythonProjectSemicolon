import random

lottery = random.randint(0, 99)
guess = eval(input("Enter your Lottery pick (two digit)\n"))

lotteryFirstDigit = lottery // 10
lotterySecondDigit = lottery % 10

guessFirstDigit = guess // 10
guessSecondDigit = guess % 10

if guess == lottery:
    print("Exact Match: you win $10,000")
elif guessFirstDigit == lotterySecondDigit and lotteryFirstDigit == guessSecondDigit:
    print("Matches all digits: you win $3000")
elif (guessFirstDigit == lotteryFirstDigit
      or guessSecondDigit == lotterySecondDigit
      or guessSecondDigit == lotteryFirstDigit
      or guessFirstDigit == lotterySecondDigit):
    print("Match 1 digit: you win $1000")
else:
    print("Sorry no Match: you lose")

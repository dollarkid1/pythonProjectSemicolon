import random


def roll_dice():
    die_1 = random.randrange(1, 7)
    die_2 = random.randrange(1, 7)

    return (die_1, die_2)


def display_dice(dice):
    die_1, die_2 = dice
    print(f' {die_1} + {die_2} = {sum(dice)} ')


dice_value = roll_dice()
display_dice(dice_value)

sum_of_dice = sum(dice_value)

if sum_of_dice in (7, 11):
    game_status = "WON"
elif sum_of_dice in (2, 3, 12):
    game_status = "LOST"
else:
    game_status = "CONTINUE"
    my_point = sum_of_dice
    print("your point is "+str(my_point))

    while game_status == "CONTINUE":
        dice_value = roll_dice()
        display_dice(dice_value)

        sum_of_dice = sum(dice_value)

        if sum_of_dice == my_point:
            game_status = "WON"
        elif sum_of_dice == 7:
            game_status = "LOST"

if game_status == "WON":
    print("Congrats You WON")
else:
    print("You LOST try again")
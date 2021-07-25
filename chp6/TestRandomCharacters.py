import RandomCharaters


def printRandomCharacters():
    NUMBERS_OF_CHARS = 175
    CHARS_PER_LINE = 25

    for i in range(NUMBERS_OF_CHARS):
        print(RandomCharaters.getRandomUpperCharacter() + " ", end=" ")
        if (i + 1) % CHARS_PER_LINE == 0:
            print()


printRandomCharacters()

print()


def print_random_btw_B_to_M():
    print(RandomCharaters.getRandomCharacters("B", "M"))


print_random_btw_B_to_M()

from random import randint


def getRandomCharacters(ch1, ch2):
    return chr(randint(ord(ch1), ord(ch2)))


def getRandomLowerCharacter():
    return getRandomCharacters('a', 'z')


def getRandomUpperCharacter():
    return getRandomCharacters('A', 'Z')


def getRandomDigitCharacter():
    return getRandomCharacters('0', '9')


def getRandomASCIICharacter():
    return chr(randint(0, 127))

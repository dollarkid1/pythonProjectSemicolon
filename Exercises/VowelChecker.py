def check():
    print("Vowel Checker")
    word = input("Enter a word \n")
    vowel = ['a', 'e', 'i', 'o', 'u']
    ver = False
    for i in vowel:
        if i in word:
            ver = True

    if ver == True:
        print("Contains Vowel")
    if ver == False:
        print("No Vowel")


check()

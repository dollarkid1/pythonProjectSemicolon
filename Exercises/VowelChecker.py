def check():
    print("Vowel Checker")
    word = input("Enter a word \n").lower()
    vowel = 'a' or 'e' or 'i' or 'o' or 'u'
    if vowel in word:
        print("Contains Vowel")
    else:
     print("No Vowel")

check()

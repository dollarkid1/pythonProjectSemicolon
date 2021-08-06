result = []
question = ["Question 1. \n A. expend energy, enjoy groups \n B. conserve energy, enjoy one-on-one",
            "Question 2\n. A. interpret literally \n B. look for meaning and possibilities",
            "Question 3.\n A. logical, thinking, questioning\n B. empathetic, feeling, accommodating",
            "Question 4.\n A. organized, orderly or b. flexible, adaptable",
            "Question 5.\n A. more outgoing, think out loud \n B. more reserved, think to yourself",
            "Question 6.\n A. practical, realistic, experiential \n B. imaginative, innovative, theoretical",
            "Question 7.\n A. candid, straight forward, frank \n B. tactful, kind, encouraging",
            "Question 8.\n A. plan, schedule \n B. unplanned, spontaneous",
            "Question 9.\n A. seek many tasks, public activities, interaction with others\n  B. seek private, "
            "solitary activities with quiet to concentrate\n",
            "Question 10.\n A. standard, usual, conventional \n B. different, novel, unique",
            "Question 11.\n A. firm, tend to criticize, hold the line \n B. gentle, tend to appreciate, conciliate",
            "Question 12.\n A. regulated, structured \n B. easygoing, “live” and “let live”\n",
            "Question 13.\n A. external, communicative, express yourself \n B. internal, reticent, "
            "keep to yourself",
            "Question 14.\n A. focus on here-and-now \n B. look to the future, global perspective, “big picture”\n",
            "Question 15.\n A. tough-minded, just \n B. tender-hearted, merciful",
            "Question 16.\n A. preparation, plan ahead \n B. go with the flow, adapt as you go\n",
            "Question 17.\n A. active, initiate \n B. reflective, deliberate\n",
            "Question 18.\n A. facts, things, “what is” \n B. ideas, dreams, “what could be,” philosophical",
            "Question 19.\n A. matter of fact, issue-oriented \n B. sensitive, people-oriented, compassionate",
            "Question 20.\n A. control, govern \n B. latitude, freedom"]
answers = []
for i in question:
    print(i)
    answer = str(input("Enter your Answer\n"))
    while answer.lower() != "a" or answer.lower() != "b":
        answer = str(input("Enter 'a or b'"))
    answers.append(answer)

print(answers)
a = 0
b = 0
for value in range(0, 16, 4):
    if 'a'.upper() or 'A'.lower() in answers:
        a += 1
    else:
        b += 1
if a > b:
    result.append("E")
else:
    result.append("I")

for value in range(1, 15, 4):
    if 'a'.upper() or 'A'.lower() in answers:
        a += 1
    else:
        b += 1
if a > b:
    result.append("S")
else:
    result.append("N")

for value in range(2, 18, 4):
    if 'a'.upper() or 'A'.lower() in answers:
        a += 1
    else:
        b += 1
if a > b:
    result.append("T")
else:
    result.append("F")

for value in range(3, 19, 4):
    if 'a'.upper() or 'A'.lower() in answers:
        a += 1
    else:
        b += 1
if a > b:
    result.append("J")
else:
    result.append("P")

print(result)
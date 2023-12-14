ques = [
    [
        "sunlight has the important source of vitamins that is?",
        "vitamin a",
        "vitamins b",
        " vitamins c",
        "vitamin d",
        4,
    ],
    [
        "sunlight has the important source of vitamins that is?",
        "vitamin a",
        "vitamins b",
        " vitamins c",
        "vitamin d",
        4,
    ],
    [
        "sunlight has the important source of vitamins that is?",
        "vitamin a",
        "vitamins b",
        " vitamins c",
        "vitamin d",
        4,
    ],
]
level = [1000, 2000, 5000, 8000, 10000, 20000, 30000, 40000, 500000]
money = 0
for i in range(0, len(ques)):

    question = ques[i]
    print(f"\n\nQuestion for Rs. {level[i]}")
    print(f"a. {question[1]}       b. {question[2]}")
    print(f"c. {question[3]}       d. {question[4]}")

    reply = int(input("Enter your answer (1-4) or  0 to quit:\n"))
    if (reply == 0):
        money = level[i - 1]
        break
    if (reply == question[-1]):
        print(f"your answer is correct, you have won: {level[i]}")
    elif (i == 4):
        money = 10000
    elif (i == 6):
        money = 30000
    elif (i == 8):
        money = 500000
    else:
        print("wrong answer!")
        break


print(f"yout take home money is {money}")

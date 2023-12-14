import random
name = input("enter your name : ")
print(f"Welcome {name} into snake, water and gun game")
print("-------------------------------------")
while True:

    userchoice = input(
        "enter your choice :-\n1 \ snake\n2 \ gun\n3 \ water\nyour choice :- ")
    print(" -------------------------------")
    if (userchoice == '1'):
        print("you choose : snake")
    elif (userchoice == '2'):
        print("you choose : gun")
    elif (userchoice == '3'):
        print("you choose : water")

    pcitem = ['snake', 'water', 'gun']
    computerchoice = random.choice(pcitem)
    print("computer choice is : ", computerchoice)

    if (userchoice == '1' and computerchoice == 'water'):
        print("congratulation , you win a game")
        print("----------------------------------")
    elif (userchoice == '3' and computerchoice == 'gun'):
        print("congratulatiom , you win a game")
        print("----------------------------------")
    elif (userchoice == '2' and computerchoice == 'snake'):
        print("congratulation , you win a game")
        print("----------------------------------")
    elif userchoice == pcitem:
        print("tie")

    else:
        print("computer wins , you lose ")
        print("----------------------------------")

    playagain = input("play again? (y/n) :")
    if playagain.lower() != 'y':
        break

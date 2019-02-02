from random import randint


def userChoice(choice):
    if choice == 1:
        return "rock"
    elif choice == 2:
        return "paper"
    elif choice == 3:
        return "scissors"
    else:
        raise Exception("Should not reach here")


def computerChoice():
    choice = randint(1, 3)
    if choice == 1:
        return "rock"
    elif choice == 2:
        return "paper"
    elif choice == 3:
        return "scissors"
    else:
        raise Exception("Should not reach here")


def chooseWinner(user, computer):
    user = user.lower()

    valid_choices = ["rock", "paper", "scissors"]
    if user not in valid_choices or computer not in valid_choices:
        raise Exception("Invalid choice has been made")
    if user == "rock":
        if computer == "paper":
            result = "You lost"
        elif computer == "scissors":
            result = "You won"
        else:
            result = "It's a tie"

    elif user == "paper":
        if computer == "scissors":
            result = "You lost"
        elif computer == "rock":
            result = "You won"
        else:
            result = "It's a tie"

    elif user == "scissors":
        if computer == "rock":
            result = "You lost"
        elif computer == "paper":
            result = "You won"
        else:
            result = "It's a tie"
    else:
        raise Exception("Should never reach here")

    print(result)


def theGame():
    print("Welcome to rock paper scissors")
    print("\tRock: 1")
    print("\tPaper: 2")
    print("\tScissors: 3")
    print()
    choice = int(input("Enter 1,2, or 3: "))
    user = userChoice(choice)
    computer = computerChoice()
    chooseWinner(user, computer)

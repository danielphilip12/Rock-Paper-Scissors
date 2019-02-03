from random import randint

def userChoice(choice):
    if (choice == 1):
        return "rock"
    elif choice == 2:
        return "paper"
    elif choice == 3:
        return "scissors"
    elif choice == 4:
        return "lizard"
    elif choice == 5:
        return "spock"
    else:
        raise Exception("Should not reach here")

def computerChoice():
    choice = randint(1, 5)
    if (choice == 1):
        return "rock"
    elif choice == 2:
        return "paper"
    elif choice == 3:
        return "scissors"
    elif choice == 4:
        return "lizard"
    elif choice == 5:
        return "spock"
    else:
        raise Exception("Should not reach here")

def chooseWinner(user, computer):
    user = user.lower()

    valid_choices = ["rock", "paper", "scissors", "lizard", "spock"]
    if user not in valid_choices or computer not in valid_choices:
        raise Exception("Invalid choice has been made")
    if user == "rock":
        if computer == "paper" or computer == "spock":
            result = "You lost"
        elif computer == "scissors" or computer == "lizard":
            result = "You won"
        else:
            result = "It's a tie"

    elif user == "paper":
        if computer == "scissors" or computer == "lizard":
            result = "You lost"
        elif computer == "rock" or computer == "spock":
            result = "You won"
        else:
            result = "It's a tie"

    elif user == "scissors":
        if computer == "rock" or computer == "spock":
            result = "You lost"
        elif computer == "paper" or computer == "lizard":
            result = "You won"
        else:
            result = "It's a tie"
    elif user == "lizard":
        if computer == "scissors" or computer == "rock":
            result = "You lost"
        elif computer == "spock" or computer == "paper":
            result = "You won"
        else:
            result = "It's a tie"
    elif user == "spock":
        if computer == "lizard" or computer == "paper":
            result = "You lost"
        elif computer == "rock" or computer == "scissors":
            result = "You won"
        else:
            result = "It's a tie"
    else:
        raise Exception("Should never reach here")

    print(result)

def theGame():
    while True:
        try:
            print("Welcome to rock paper scissors")
            print("\tRock: 1")
            print("\tPaper: 2")
            print("\tScissors: 3")
            print("\tLizard: 4")
            print("\tSpock: 5")
            print()
            choice = int(input("Enter 1, 2, 3, 4, or 5: "))
            if choice > 5:
                raise Exception()
            break
        except:
            print("Enter valid number")
    user = userChoice(choice)
    computer = computerChoice()
    chooseWinner(user, computer)
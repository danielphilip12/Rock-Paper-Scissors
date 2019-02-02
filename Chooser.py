import RockPaperScissors
import RockPaperScissorsLizardSpock



while(True):
    print('Choose your game')
    print("")
    print("\tRock, Paper, Scissors: 1")
    print("\tRock, Paper, Scissors, Lizard, Spock: 2")
    print("")
    game = int(input("Which one(1 or 2): "))
    if game == 1:
        RockPaperScissors.theGame()
    elif game == 2:
        RockPaperScissorsLizardSpock.theGame()
    else:
        print("Invalid number")
    
    print("Would you like to play again?")
    again = str(input("Yes or No(Y or N): "))
    if again == "Y" or again == "y":
        continue
    else:
        break
    
import random

options = ["rock", "paper", "scissors"]

com = random.choice(options)
userChoice = None
comCount = 0
userCount = 0
tieCount = 0

while userChoice not in options and userChoice != "stop":
    userChoice = input("rock, paper, or scissors? if you want to quit playing type stop.: ").lower()
while userChoice != "stop":
    match userChoice:
        case "stop":
            quit()
        case "rock":
            if userChoice == com:
                print("user: ", userChoice)
                print("com: ", com, "\nStalemate!!!")
                print("===============================================================================================")
                tieCount += 1
            elif com == "paper":
                print("user: ", userChoice)
                print("com: ", com, "\nYou Lose!!!")
                print("===============================================================================================")
                comCount += 1
            elif com == "scissors":
                print("user: ", userChoice)
                print("com: ", com, "\nYou Win!!!")
                print("===============================================================================================")
                userCount += 1

        case "paper":
            if userChoice == com:
                print("user: ", userChoice)
                print("com: ", com, "\nStalemate!!!")
                print("===============================================================================================")
                tieCount += 1
            elif com == "scissors":
                print("user: ", userChoice)
                print("com: ", com, "\nYou Lose!!!")
                print("===============================================================================================")
                comCount += 1
            elif com == "rock":
                print("user: ", userChoice)
                print("com: ", com, "\nYou Win!!!")
                print("===============================================================================================")
                userCount += 1

        case "scissors":
            if userChoice == com:
                print("user: ", userChoice)
                print("com: ", com, "\nStalemate!!!")
                print("===============================================================================================")
                tieCount += 1
            elif com == "rock":
                print("user: ", userChoice)
                print("com: ", com, "\nYou Lose!!!")
                print("===============================================================================================")
                comCount += 1
            elif com == "paper":
                print("user: ", userChoice)
                print("com: ", com, "\nYou Win!!!")
                print("===============================================================================================")
                userCount += 1
    userChoice = input("rock, paper, or scissors? if you want to quit playing type stop.: ").lower()

print("Stalemates: ", tieCount)
print("Computer wins: ", comCount)
print("User wins: ", userCount)


if comCount == userCount :
    print("\nRNG gave equal chances today?!?!?Or this game is just not your cup of tea?")
elif comCount > userCount:
    print("\nYou lose the RNG battle!")
elif comCount < userCount:
    print("\nYou win the RNG battle!")

print("This is your success ratio:", userCount/comCount)
print("This is the computer's success ratio:", comCount/userCount)
print("This the stalemate ratio:", tieCount/(comCount+userCount))
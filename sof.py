
def printGame():
    print("Welcome to Smoke or Fire")
    print("Type QUIT during your turn to end the game")
    print("If you ever want to show current cards in play type \"show\"")

#this will take in and return GameState
def game(gameState):
    while gameState.turn():
        while True:
            if gameState.noCardsInPlay():
                printMainChoices()
            else:
                printAllChoices(gameState.lastCard())
            choice = input()
            choice = choice.lower()
            if(checkInput(choice)):
                break
            elif(choice == "show"):
                for Card in gameState.inPlay():
                    print(Card)
            elif(choice == 'quit'):
                break
            else:
                print("Invalid Choice")

        if(choice == 'quit'):
            break

        newCard = gameState.getCard()
        print(newCard);
        if( gameState.checkGuess(choice, newCard) ):
            print("Correct!")
        else:
            print ("Incorrect!")

        if gameState.checkSameCard():
            print("everyone else owes a shot!")
            gameState.setPassed(True)
            continue
        
        if (drinks := gameState.owedDrinks()) > 0:
            print(str(drinks) + " drinks bitch!")

 

def printGame():
    print("Welcome to Smoke or Fire")
    print("Type \"quit\" during your turn to end the game")
    print("If you ever want to show current cards in play type show")
        

def printMainChoices():
    print("Smoke (s) or Fire (f)")

def printAllChoices(card):
    print("Current Card: " + str(card))
    print("Smoke (s) or Fire (f), Higher (h) or Lower (l), Same Card (sc)")

def checkInput(choice):
    if(choice == "s"):
        return True
    elif(choice == "f"):
        return True
    elif(choice == "h"):
        return True
    elif(choice == "l"):
        return True
    elif(choice == "sc"):
        return True
    else:
        return False
# This is game called smoke or fire.
# This is a drinking game where the player has a number of guesses to make on the next card in the deck. Depending on the tern the player will have more or less options 
# to choose from. If the player is starting from an uncontinued state then they will have to get 4 guesses in a row correct to pass the game onto the next player. If they are
# continuing from a previous state then they will have to get 3 guesses in a row correct to pass the game onto the next player. The amount of drinks corresponds to the amount of 
# guesses they have made in a row correct.
# Types of guesses:
# 1. smoke - this corresponds to the card being black (can be used from any game state)
# 2. fire - this corresponds to the card being red (can be used from any game state)
# 3. higher - this corresponds to the card being higher than the previous card (can only be used from a continued game state)
# 4. lower - this corresponds to the card being lower than the previous card (can only be used from a continued game state)
# 5. same card - this corresponds to the card being the same as the previous card. If a player guesses same card correctly then their turn is automatically passed
# passed and all other players have to take a shot instead of a normal drink. (can only be used from a continued game state)

# if a player can choose to continue playing instead of passing, at this point they can as long as the amount of cards in play are 4 or greater they can pass at any time.
# if the deck runs out of cards it will reshuffle without the cards that are currently in play.


# This is the main game loop, it will run until a player passes or the player types QUIT 

def printGame():
    print("Welcome to Smoke or Fire")
    print("Type QUIT during your turn to end the game")
    print("If you ever want to show current cards in play type \"show\"")

# this game loop will 

#this will take in and return GameState
# def game(GameState):
#     if(GameState.checkNewGame()):
#         printGame()
#     else:
#         print("Last Card: played was " + GameState.currentCard())
    
#     while(GameState.turn()):
#         if GameState.checkNewGame() or 
#         currCard = GameState.getCard()

#         if(GameState.getPassed()):
#             print("Would you like to continue playing? (Y/N)")
#             if(input() == "Y"):
#                 GameState.setContinued(True)
#             else:
#                 GameState.setContinued(False)
#                 break
        

#         while True:
#             printChoices()
#             input = input().lower()
#             if(checkInput(input)):
#                 break

#             elif(input == "show"):
#                 for Card in GameState.inPlay():
#                     print(Card)
#             else:
#                 print("Invalid Choice")


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
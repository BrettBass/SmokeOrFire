#a deck object is created to hold a list of cards
#it will hold the cards in play, ready to play, and the cards that have been played
import random
import card.py

class Deck:
    def __init__(self):
        self.cards = []
        self.discard = []
        self.inPlay = []
        self.buildDeck()
        self.shuffle()
    
    def buildDeck(self):
        for suit in ["Spades", "Hearts", "Clubs", "Diamonds"]:
            for value in range(1, 14):
                self.cards.append(Card(suit, value))
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self):
        if len(self.cards) == 0:
            #this could break if discard is empty
            self.cards = self.discard
            self.discard = []
            self.shuffle()
        Card = self.cards.pop()
        self.inPlay.append(Card)
        return Card
    
    def discard(self, Card):
        self.discard.append(Card)
        self.inPlay.remove(Card)

    def displayInPlay(self):
        for Card in self.inPlay:
            print(Card)
    
    def printCurrentCard(self):
        if len(self.inPlay) > 0:
            print(self.inPlay[-1])
        else:
            print("No cards in play")

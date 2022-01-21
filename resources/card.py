#card class used to identify playing cards
#
#

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        if self.suit == Spades or self.suit == Clubs:
            self.color = Black
        else:
            self.color = Red
    
    def __str__(self):
        return self.suit + " " + self.value
    
    def getValue(self):
        return self.value
    
    def getSuit(self):
        return self.suit
    
    def getColor(self):
        return self.color
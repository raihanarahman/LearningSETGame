colors = ["red", "purple", "green"]
shapes = ["squiggle", "oval", "diamond"]
numbers = [1, 2, 3]
fillings = ["solid", "empty", "shaded"]
deck = []

class Card:
    def __init__(self, color, shape, number, filling):
        self.color = color
        self.shape = shape
        self.number = number
        self.filling = filling
    
    # I would like to be able to return a set of all the properties of a given card. It's more convenient for when I use check()
    def info(self):
        return set([self.color, self.shape,self.number, self.filling])

def makeDeck():
    for color in colors:
        for shape in shapes:
            for number in numbers:
                for filling in fillings:
                    card = Card(color, shape, number, filling)
                    deck.append(card)
    return deck

def check(card1, card2, card3):
    # Determine all common qualities among all three cards.
    allCommon = Card.info(card1).intersection(Card.info(card2), Card.info(card3))
    # Determine all common qualities between each possible pair of cards.
    oneTwoCommon = Card.info(card1).intersection(Card.info(card2))
    oneThreeCommon = Card.info(card1).intersection(Card.info(card3))
    twoThreeCommon = Card.info(card2).intersection(card3.info())
    # If the common qualities between pairs of cards are the same as the common qualities among all three cards, a proper set has been created. Return true. 
    # Note that this means that if 0 qualities are shared, a proper set has still been made. 
    if allCommon == oneTwoCommon and oneTwoCommon == oneThreeCommon and oneThreeCommon == twoThreeCommon:
        return allCommon
    return False

def initial():
    drawn = []
    # Creates the initial arrangement of 12 cards (called drawn cards) for our user to play with. We are taking our deck of cards 
    # and selecting 12 cards such that there are 6 sets present. A set is a group of cards which either all agree or disagree on 
    # their color, shape, number, and filling. 

# One option to draw 12 cards: 
    # Use a while loop to loop through the following
        # Choose 12 random cards. 
        # Use check() to determine if there are 6 sets in the group of cards
        # If yes, then we have finished initializing. Return the group of cards and exit the loop
        # If no, loop again.
    
# Potential Issues: This can be a very inefficient way to generate groups of cards. Another method of doing so:
    # Create a database of all possible sets of three cards. Or, import such a database (to increase efficiency)
    # Choose six sets at random, and count the number of unique cards. 
        # If the number of total cards is 12, return this grouping of cards
        # If the number is less than 12, generate as many random cards as necessary to bring the total card count to 12
# There are two options if the number of cards exceeds 12: 
        # If more than 12, restart the entire process from creating/importing a database. 
        # Or, if more than 12, remove one set at random, and run through all the pairs of cards to determine if there is a third card
            # which can be added to increase the number of sets in the group without exceeding the number of drawn card. Continue with this 
            # process until card count is 12. 

# Another approach (drawback is that all sets will necessarily share a common card): 
    # Each set has qualities which are different: color, number, shading, shape, or any combination of the four. 
    # Create a list of all possible unordered combinations of the four qualities. (Ex. color and shading, number and shape, etc.)
    # Randomly choose one card. 
    # Randomly choose six combinations from the list of qualities. 
    # According to the six combinations, choose cards from the deck which can complete sets according to the qualities 
        # that must be different among all of the cards. 
        # Choose cards by first looking at the cards already selected and determine whether a new set can be made according to the given
        # quality that was chosen. For example, if a ♦️ and ♦️♦️ card are already selected, and one of the differing qualities in 
        # our list is number of items on the card, then a set can be made with ♦️♦️♦️ card. 
        # If a set cannot be made with the cards already drawn, select cards from the deck that can be used to satisfy the criteria.
    # If, after this process, the number of drawn cards is less than 12, select random cards to fill the remaining space. 
    # If the number of drawn cards is 12, return the drawn cards. 
# There are two options if the number of cards exceeds 12:
    # If the number of drawn cards is more than 12, restart the entire process
    # Or, if more than 12, remove one set at random, and run through all the pairs of cards to determine if there is a third card
            # which can be added to increase the number of sets in the group without exceeding the number of drawn card. 
            # Ensure that the initial selected card is not removed. Continue with this process until card count is 12. 

    return drawn

def game():
    foundSETs = 0
    gameboard = initial()
    # send the gameboard to the frontend for the user to play with. 
    while foundSETs != 6:
       # Take in user inputs as card1, card2, card3 for the three cards selected. 
       if check(card1, card2, card3) == True:
           foundSETs = foundSETs + 1
    return True

# Simple test case of check() method. 
card1 = Card("red", "oval", 1, "solid")
card2 = Card("purple", "squiggle", 2, "empty")
card3 = Card("green", "diamond", 3, "shaded")
print(check(card1, card2, card3))

makeDeck()
print(deck[23].info())
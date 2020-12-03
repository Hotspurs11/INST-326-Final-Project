class Card:
    """Card game. Assigns values for each card including number and suit
   Attributes:
   value(int) is the numerical value of the card
   suit(str) is the suit of the card
    """
    suits = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
    ranks = ('narf', 'Ace', '2', '3', '4', '5', '6', '7',
             '8', '9', '10', 'Jack', 'Queen', 'King']
    
    def __init__(self, suit=0, rank=0):
    """the __init__function here creates a value for each card and assign a suit
    Args: 
        suit(str): suit of the card
        rank(str): number on the card
    Returns: N/a
    Raises: N/A
    Side Effects: N/A
    """
        self.suit = suit
        self.rank = rank

    def __str__(self):
    """the __str___ function will return a statement that states the name of the card and its suit
          >>> print(Card(2, 11))
          Queen of Hearts
    Args: self
    Returns: rank and suit of card
    Raises: N/A
    Side Effects: N/A
    """
        return self.rank + 'of' + self.suit
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()    
class Deck:
    """ Makes a deck of cards and takes a card if there are cards left
    """
    def __init__(self):
        """the __init___ fucntion here creates a list of suits and the number of cards. Then, it shuffles the card using an imported shuffle statement
        """
    
    def ___draw___(self):
        """the draw function takes the entire length of the list and when its greater than zero it will return a card.
        Raises: RunTimeErro if less than zero
        """
        
        
class Main:
    """Starts the game and asks for dollar amount from both players. Creates 53 card deck instance which includes 1 joker
    """
    def __init__(self):
    
def joker():
    """If either person has a joker then the highest hand wins 
    Raises: N/A
    Side Effects: N/A
    """

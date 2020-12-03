class Card:
    """Card game. Assigns values for each card including number and suit
   Attributes:
   value(int) is the numerical value of the card
   suit(str) is the suit of the card
    """
    def __init__(self,value,suit):
    """the __init__function here creates a value for each card and assign a suit
    """

    def __str__(self):
    """the __str___ function will return a statement that states the name of the card and its suit
    """
        
        
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
class Player:
    ''' This class is responsible for the player. Anything that has to deal with the player. You can fold, bet, doubledown and draw with this class.
    Args: N/A
    Returns: N/A
    Raises: N/A
    Side Effects: N/A '''
    def __init__(self, balance, name, handvalue):
        ''' Defines variables of the player object
        Args: N/A
        Returns: N/A
        Raises: N/A
        Side Effects: N/A'''
    def fold():
        ''' Folds players hand
        Args: N/A
        Returns: N/A
        Raises: N/A
        Side Effects: N/A '''
    
    def draw():
        ''' Draws 1 card to players hand
        Args: N/A
        Returns: N/A
        Raises: N/A
        Side Effects: N/A '''
        
    def bet():
        ''' Bets amount specified by player
        Args: N/A
        Returns: N/A
        Raises: N/A
        Side Effects: N/A '''
        
    def doubledown():
        ''' Doubles bet
        Args: N/A
        Returns: N/A
        Raises: N/A
        Side Effects: N/A '''

class Dealer:
    """This class is responsble for dealing out the acrds to the players in the game. It should be able to deal to both human and computer players. this class will contain the deal function and the shuffle fucntion. The deal function will draw 2 cards
    for the dealer and deal 2 cards to the other player. The shuffle fucntion will shuffle the 52 card deck including the jokers to ensure randomness.
    Args: N/A
    Returns: 2 cards to each player 
    Raises: N/A
    Side Effects: N/A"""
    
    def deal():
        """this fucntion will be rsponsible for drawing and dealing the 2 cards for each player. it will take cards from the shuffled cards.
        Args: N/A
        Returns: 2 cards for each player playing (4 cards in total)
        Raises:N/A
        Side effects: N/A"""
        
    def shuffle():
        """This funciton is responsible for shuffling the cards each game so that the game remians fair and random. This function will make sure to include all 52 cards including the joker. we will import the shuffle fucntion from random
        Args: shuffle 
        Returns: a deck of 52 cards that are shuffled
        Raises: N/A
        Side effects: N/A


def update():
    """
    store users scores from previous functions and intialize the balances of each player
    args:
        player1_score(int): the value of the score of the dealer from previous parts
        player2_score(int): the value of the score of the player
        
    return:
        int:  users current balance
    """

def endgame():
    """
    Compares the hand value to dealer value and presents a winner of the overall game
    args:  
        hand(int): stores hand value to dealer value    
    returns:
       list of str:  representation of the end balance of the player, indicaiting winner of game
    Side Effects: 
        modifies score   
       
    """
    
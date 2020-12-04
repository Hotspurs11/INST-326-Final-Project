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
# Wilson's code
class player():
    ''' This class is responsible for the player. Anything that has to deal with the player. You can fold, bet, doubledown and draw with this class.
    Args: N/A
    Returns: N/A
    Raises: N/A
    Side Effects: N/A '''             
    def __init__(self,balance,name,hand_value):
    ''' Defines variables of the player object
    Args: balance, name, hand_value
    Returns: N/A
    Raises: N/A
    Side Effects: N/A'''         
        self.balance = balance
        self.name = name
        self.hand_value = hand_value   
        
    def fold(self):
    ''' Folds players hand
        Args: N/A
        Returns: N/A
        Raises: N/A
        Side Effects: Removes placed bet from balance losing round '''         
        self.balnce = self.balance - player
            
    def draw(self):
    ''' Draws 1 card to players hand
        Args: N/A
        Returns: Returns new hand value after random card is drawn
        Raises: N/A
        Side Effects: N/A '''         
        new_card = Card()
        self.hand_value = self.hand_value + new_card.value
        return self.hand_value
    
    def bet(self,player_bet):
    ''' Bets amount specified by player
        Args: player_bet, bets desired amount inputted by user
        Returns: N/A
        Raises: N/A
        Side Effects: Prints insufficient funds when player balance isn't enough '''
        if player_bet > self.balance:
            print('Insufficient funds.')
        else:
            self.balance = self.balance - player_bet
         
    def double_down(self,player_bet):
    ''' Doubles bet
        Args: player_bet
        Returns: N/A
        Raises: N/A
        Side Effects: Prints insufficient funds when player balance isn't enough '''
        double_down2 = player_bet * 2
        if double_down2 < self.balance:
            print('insufficient funds.')
        else:
            self.balance = self.balance - double_down2
# end Wilson's code
from random import shuffle
class Shuff:
    """This class is responsble for dealing out the acrds to the players in the game. It should be able to deal to both human and computer players. this class will contain the deal function and the shuffle fucntion. The deal function will draw 2 cards
    for the dealer and deal 2 cards to the other player. The shuffle fucntion will shuffle the 52 card deck including the jokers to ensure randomness.
    Args: N/A
    Returns: 2 cards to each player 
    Raises: N/A
    Side Effects: N/A"""  
        
    def shuffle(self):
        """This funciton is responsible for shuffling the cards each game so that the game remians fair and random. This function will make sure to include all 53 cards including the joker. we will import the shuffle fucntion from random
        Args: shuffle 
        Returns: a deck of 53 cards that are shuffled
        Raises: N/A
        Side effects: N/A"""
        card_list = 4 * [x for x in range(2, 12)] + 12 * [10] + 1
        random.shuffle(card_list)

        self.top = None

        for card in card_list:
            new_card = self.Shuff(card)
            new_card.next = self.top
            self.top = new_card

    def __repr__(self):
        curr = self.top
        out = ""
        card_list = []
        while curr is not None:
            card_list.append(str(curr.value))
            curr = curr.next

        return " ".join(card_list)
    def draw(self):
        """Returns the top card of the deck and sets @self.top to the next card"""
        

        drawnCard = self.top.value
        self.top = self.top.next
        return drawnCard

class Dealer(Player):
    def signal_hit(self, player):
        """
        A method called by players when they want to hit
        Player objects should pass their `self` references to this method
        Should deal one card to the player that signalled a hit"""
        
        player.deal_to(self.deck.draw())

    #If the dealer's hand is 16 or below, the dealer hits - stands otherwise
    def play_round(self):
        """
        A dealer should hit if his hand totals to 16 or less"""

        handSum = self.card_sum
        while handSum < 17:
            self.signal_hit(self)
            handSum = self.card_sum



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
    

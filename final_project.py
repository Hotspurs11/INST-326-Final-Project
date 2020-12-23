import sys
import doctest
from random import seed
from random import randint
import random
class Card:
  
    
    def __init__(self, suit=0, value=0):
        """the __init__function here creates a value for each card and assign a suit
        Args: 
            suit(str): suit of the card
            rank(str): number on the card
        Returns: N/a
        Raises: N/A
        Side Effects: N/A
        
        """    
        self.suit = suit
        self.value = value
    def __repr__(self):
        """returns the card that would change"""
        return " of ".join((self.value, self.suit))   


class Deck:
    
    """Card game. Assigns values for each card including number and suit. contians 52 unique cards needed to be shuffled using out shuffle and error
    functions. we use the pop fucntion of a list to return back the top card and remove it from the deck.
   value(int) is the numerical value of the card
   suit(str) is the suit of the card"""
   
    def __init__(self):
        """Assigns values to the card"""
        self.cards= [Card(types,numbers) for types in ["Spades", "Clubs", "Hearts", "Diamonds"] for numbers
                    in ["Ace", "2", "3","4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]]
        
    def shuffle(self):
        """ This function is in charge of shuffling the cards"""
        if len(self.cards) > 1:
            random.shuffle(self.cards)
   
    def error(self):
        """ When there's no cards to be played, this function will raise an error"""
        if len(self.cards) == 0:
            raise RuntimeError
              
    def deal(self):
        """this function will use th epop method to return the top card"""
        if len(self.cards) > 1:
            return self.cards.pop()
            
        

class Player:
    ''' This class is responsible for the player. Anything that has to deal with the player.
    You can fold, bet, doubledown and draw with this class.
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
        self.balance = int(balance)
        self.name = name
        self.hand_value = hand_value   
        self.foldround = False
        
    def fold(self):
        ''' Folds players hand
        Args: N/A
        Returns: N/A
        Raises: N/A
        Side Effects: Removes placed bet from balance losing round 
        '''         
        return self.foldround
        
            
    
    def bet(self,player_bet):
        ''' Bets amount specified by player
        Args: player_bet, bets desired amount inputted by user
        Returns: N/A
        Raises: N/A
        Side Effects: Prints insufficient funds when player balance isn't enough 
        '''
        if int(player_bet) > self.balance:
            print('Insufficient funds.')
            sys.exit()
        else:
            self.balance = self.balance - int(player_bet)
         
    def double_down(self,player_bet):
        ''' Doubles bet of the player
        Args: player_bet
        Returns: N/A
        Raises: N/A
        Side Effects: Prints insufficient funds when player balance isn't enough 
        '''
        double_down2 = int(player_bet) * 2
        if double_down2 > self.balance:
            print('insufficient funds.')
            sys.exit()
        else:
            self.balance = self.balance - double_down2


class player_game:
    """this function controls the rules of the game. the add card function will add a card to the list.
   the calc function will calcculate the score of each players hand based off the rules of blackjack.
   https://dev.to/nexttech/build-a-blackjack-command-line-game-3o4b this link helped us with the calc, 
   add_card, value_display, show, and player_hand functions. we had to change around some variables in
   order for the rest of the script to run well. the logic of the math was ours since its simply the rules of 
   blackjack however we felt it to be better to keep thier variables and iterators as they were referenced later on
   in the code."""
    def __init__(self, dealer = False):
        self.dealer = dealer
        self.cards = []
        self.value = 0 
    def add_card(self, card):
        """adds a card to the hand"""
        self.cards.append(card)
    
    def calc(self):
        """rules of the game, fucntion will add the value of the card to the players hand"""
        self.value = 0
        contains_ace = False
        for card in self.cards:
            if isinstance(card.value, int):
                self.value += isinstance(card.value, int)
            else:
                if card.value == "A":
                    contains_ace = True
                    self.value += 11
                else: 
                    self.value += randint(2,10) 
                    

        if self.value > 21:
            print("bust") 
    def value_display(self):
        """displays score
        Returns: (Int)Score"""
        self.calc()
        return self.value
    
    def show(self):
        """this fucntion is repsonsible for showing the hands and hiding the dealers hand"""
        if self.dealer:
            print("face down card")
            print(self.cards[1])
            
    def player_hand(self):
        """prints out the players hand"""
        for s in self.cards:
            print(s)
        print("The Value is ", self.value_display())    
                  
class Game:
    """this function is the main game loop. its what interacts with the user by asking if they want to  play again or
    what they want to do with thier turn. it will also indicate if w=either side got a blackjack.
    https://dev.to/nexttech/build-a-blackjack-command-line-game-3o4b we used this link to help create the functions
    of this class. We had to change around iterators because thier script had errors so we changed them."""
    def __init__(self):
        pass

    def play_game(self):
        """this fucntion will continue to deal and shuffle cards as long as the user wants to play.
        if the user does not want to play then it ends the game"""
        playing = True
        print('What is your name?')
        name = input()
        print('How much money will you like to start with?')
        balance = input()
        self.player_hand = player_game()
        self.dealer_hand = player_game(dealer=True)
        
        player = Player(balance, name, self.player_hand.value_display())
        print('How much would you like to bet?')
        bet = input()
        player.bet(bet)
        
        print('Do you want to doubledown? Enter 1 for yes, 0 for no.')
        doubledown = int(input())    

        temp = False
        while not temp:
            self.deck = Deck()
            self.deck.shuffle()
            for _ in range(2):
                self.player_hand.add_card(self.deck.deal())
                self.dealer_hand.add_card(self.deck.deal())
                   
            print("Current hand: ", self.player_hand.value_display())
            print("Current Dealers hand: ", self.dealer_hand.value_display())
            temp2 = False
            while not temp2: 
                print('Do you want to fold? (Stop drawing cards) Enter 1 for yes or 0 for no.')
                fold = int(input())
                if fold == 1:
                    player.foldround = True
                    temp2 = True
                else:
                    player.foldround = False
                    self.player_hand.add_card(self.deck.deal())
                    print("Current hand: ", self.player_hand.value_display())
                    print("Current Dealers hand: ", self.dealer_hand.value_display())
                    
            player_has_blackjack, dealer_has_blackjack = self.check_blackjack()
            if player_has_blackjack or dealer_has_blackjack:
                temp = True
                self.blackjack_results(
                    player_has_blackjack, dealer_has_blackjack) 
            if doubledown == 1:
                    player.double_down(int(bet))

            player_value = self.player_hand.value_display()
            dealer_value = self.dealer_hand.value_display()

            print("End Results: ")
            print("Your Cards: ", player_value)
            print("Dealer's Cards: ", dealer_value)
            if player_value > 21 and dealer_value <= 21:
                print("Sorry you lost, Dealers wins")
            elif player_value <= 21 and dealer_value > 21:
                print("You won the game!")
                if doubledown == 1:
                    player.balance += bet*4
                else:
                    player.balance += bet*2
            elif player_value < dealer_value:
                print("you lost the game")
            elif player_value == dealer_value:
                print("you tied with the dealer")
            elif player_value > dealer_value:
                print("you won the game!")           
                
            play_again = int(input("Would you like to play again? Enter 1 for Yes or 0 for No. "))
            if play_again == 0:
                print("Thank you for playing, play again soon!")
                print('Your ending balance is ', player.balance)
                temp = True                    
            else:
                print('Your current balance is ', player.balance)
                self.player_hand = player_game()
                self.dealer_hand = player_game(dealer=True)
                self.deck = Deck()
                self.deck.shuffle()
                temp = False
                                          
    def blackjack_results(self, player_blackjack, dealer_blackjack):
        """indicates if dealer or player got a blackjack and will end that round of gameplay
        Arguments: player_blackjack: Taking in the players choices, player get blackjack
                    dealer_blackjack: Dealers get blackajck """
        if player_blackjack and dealer_blackjack:
            print("Both have blackjack")

        elif player_blackjack:
            print("You got blackjack, you win!")

        elif dealer_blackjack:
            print("Dealer got blackjack, you lose") 
        player_choice = input("Please choose hit or stay ").lower()
        while player_choice not in [ "hit", "stay"]:
            player_choice = input("enter hit or stay ").lower()
        if player_choice in ['hit']:
            self.player_hand.add_card(self.deck.deal())
            self.player_hand.player_hand()
    def player_is_over(self):
        """indicates if the player is over the score of 21
        Returns: If players score is over 21"""
        return self.player_hand.value_display() > 21                        
               
    def check_blackjack(self):
        """this function will check for a blackjack
        Returns: If player won or dealer won"""
        player = False
        dealer = False
        if self.player_hand.value_display() == 21:
            player = True
        if self.dealer_hand.value_display() == 21:
            dealer = True

        return player, dealer 
if __name__ == "__main__":
    game = Game()
    game.play_game()              

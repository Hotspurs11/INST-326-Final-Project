import doctest
import random

class Card:
   
    
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
    def __repr__(self):
        return " of ".join((self.rank, self.suit))   


class Deck:
    
    """Card game. Assigns values for each card including number and suit
   Attributes:
   value(int) is the numerical value of the card
   suit(str) is the suit of the card
    """
    def __init__(self):
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
        self.balance = balance
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
        return self.fold
        
            
    
    def bet(self,player_bet):
        ''' Bets amount specified by player
        Args: player_bet, bets desired amount inputted by user
        Returns: N/A
        Raises: N/A
        Side Effects: Prints insufficient funds when player balance isn't enough 
        '''
        if player_bet > self.balance:
            print('Insufficient funds.')
        else:
            self.balance = self.balance - player_bet
         
    def double_down(self,player_bet):
        ''' Doubles bet
        Args: player_bet
        Returns: N/A
        Raises: N/A
        Side Effects: Prints insufficient funds when player balance isn't enough 
        '''
        double_down2 = player_bet * 2
        if double_down2 < self.balance:
            print('insufficient funds.')
        else:
            self.balance = self.balance - double_down2


class player_game:
    def __init__(self, dealer = False):
        self.dealer = dealer
        self.cards = []
        self.value = 0 
    def add_card(self, card):
        self.cards.append(card)
    
    def calc(self):
        self.value = 0
        contains_ace = False
        for card in self.cards:
            if card.value.isnumeric():
                self.value += int(card.value)
            else:
                if card.value == "A":
                    contains_ace = True
                    self.value += 11
                else:
                    self.value += 10

        if contains_ace and self.value > 21:
            self.value -= 10 
    def value_display(self):
        self.calc()
        return self.value
    
    def show(self):
        if self.dealer:
            print("face down card")
            print(self.cards[1])
            
    def player_hand(self):
        for s in self.cards:
            print(s)
        print("The Value is ", self.value_display())    
                  
class Game:
    def __init__(self):
        pass

    def play_game(self):
        playing = True

        while playing:
            self.deck = Deck()
            self.deck.shuffle()

            self.player_hand = player_game()
            self.dealer_hand = player_game(dealer=True)

            for _ in range(2):
                self.player_hand.add_card(self.deck.deal())
                self.dealer_hand.add_card(self.deck.deal())

            print("Current hand: ", self.player_hand.value_display())
            print("Current Dealers hand: ", self.dealer_hand.value_display())
            end_game = False
            
            print('What is your name?')
            name = input()
            print('How much money will you like to start with?')
            balance = input()
            player = Player(balance, name, self.player_hand.value_display())
            print('How much would you like to bet?')
            bet = input()
            player.bet(bet)
            

        while not end_game:
            player_has_blackjack, dealer_has_blackjack = self.check_blackjack()
            print('Do you want to fold? (Stop drawing cards) Enter 1 for yes or 0 for no.')
            fold = int(input())
            if fold == 1:
                player.foldround = True
            else:
                player.foldround = False
                print('Do you want to doubledown? Enter 1 for yes, 0 for no.')
                doubledown = int(input())
            
            
                
       
        if player_has_blackjack or dealer_has_blackjack:
            end_game = True
            self.blackjack_results(
                player_has_blackjack, dealer_has_blackjack) 
        if doubledown == 1:
                self.player_hand.add_card(self.deck.deal())
                player.double_down(bet)
        if self.player_is_over():
                        print("You have lost!")
                        end_game = True
        else:
                    player_value = self.player_hand.value_display()
                    dealer_value = self .dealer_hand.value_display()

                    print("End Results: ")
                    print("Your Cards: ", player_value)
                    print("Dealer's Cards: ", dealer_value)

                    if player_value > dealer_value:
                        print("You won the game!")
                        if doubledown == 1:
                            player.balance += bet*4
                        else:
                            player.balance += bet*2
                    elif player_value == dealer_value:
                        print("You tied with Dealer")
                    else:
                        print("Sorry you lost, Dealers wins")
                    end_game = True
        play_again = input("Would you like to play again? Write Yes or No ")
        while play_again.lower() not in ["Yes", "No"]:
            play_again = input(" Enter Yes or No ")
        if play_again.lower() == "No":
            print("Thank you for playing, play again soon!")
            playing = False
        else:
            end_game = False                
                
                           
    def blackjack_results(self, player_blackjack, dealer_blackjack):
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
        return self.player_hand.value_display() > 21                        
               
    def check_blackjack(self):
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
  
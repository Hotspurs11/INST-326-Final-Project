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

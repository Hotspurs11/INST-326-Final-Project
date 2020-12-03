# Wilson Badillo

class player():
    def __init__(self,balance,name,hand_value):
        self.balance = balance
        self.name = name
        self.hand_value = hand_value   
        
    def fold(self):
        self.balnce = self.balance - player
            
    def draw(self):
        new_card = preethascardclass()
        self.hand_value = self.hand_value + new_card.value
        return self.hand_value
    
    def bet(self,player_bet):
        if player_bet > self.balance:
            print('Insufficient funds.')
        else:
            self.balance = self.balance - player_bet
         
    def double_down(self,player_bet):
        double_down2 = player_bet * 2
        if double_down2 < self.balance:
            print('insufficient funds.')
        else:
            self.balance = self.balance - double_down2
        
    
    
    
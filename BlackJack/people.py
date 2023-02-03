
from deck import Deck
import chip
import sys
import time

class Player() :
    def __init__(self, name, money) :
        self.name = name
        self.initial_money = money
        self.money = money
        self.chips = chip.convert_to_chips(money)
        self.hand = [[]]
        self.bet = 0
        self.did_double_down = False

    def accept_card(self, card, hand_index=0) :
        self.hand[hand_index].append(card)

    def adjust_money(self, adjustment) :
        self.money += adjustment
        self.chips = chip.convert_to_chips(self.money)

    def return_cards(self) :
        self.hand = [[]]


    def hand_value(self, hand_index=0) :  
        total = 0
        num_aces = 0
        for card in self.hand[hand_index] :
            if card.number == 1 : 
                num_aces += 1
            else :
                total += card.get_value()   
        hand_tuple = Player.place_aces(total, num_aces)
        if hand_tuple[0] :
            return hand_tuple[1]
        else :
            return total

    def place_aces(total, aces) :
        if not aces :
            return (True,total)        
        for val in [11,1] : # try 11 first so we can ensure greatest possible hand value
            if total+val <= 21 :
                total_tuple = Player.place_aces(total+val, aces-1)
                if total_tuple[0] :
                    return total_tuple
        return (False,1000) # the 1000 is just to allow method to return a tuple and also show that hand was a bust

    def check_bust(self, hand_index=0) :
        return self.hand_value(hand_index) > 21

    def check_blackjack(self, hand_index=0) :
        return self.hand_value(hand_index) == 21

    def check_broke(self) :
        return self.money == 0

    def __str__(self) :
        return f'Name: {self.name}, Account: {self.money}, Chips: {self.chips}, Hand: {self.hand}, Current Bet: {self.bet}'

class Dealer(Player) :
    def __init__(self) :
        Player.__init__(self, 'Dealer', 0) # money doesn't matter for dealer
        self.deck = Deck(6) # getting 6 decks of cards

    def deal_card(self, player, hand_index=0) :
        try :
            player.accept_card(self.deck.get_card(), hand_index)
        except : 
            print('No more cards left in deck.\nShuffling ', end='')
            for i in range(0,3) :
                print('.', end='')
                sys.stdout.flush()
                time.sleep(0.5)
            self.deck = Deck(6)
            print('Done! Resume dealing.')
            sys.stdout.flush()
            time.sleep(0.8)
            player.accept_card(self.deck.get_card(), hand_index)

    def adjust_money(self, adjustment) :
        raise TypeError('\'adjust_money()\' should not be called on object of type \'Dealer\'.')

    def retrieve_cards(self, player) :
        player.return_cards()

    def check_hard_17(self, hand_index=0) :
        total = 0
        for card in self.hand[hand_index] :
            total += card.get_value()
        return total >= 17

    def __str__(self) :
        personInfo = Player.__str__(self)
        return f'{personInfo} {self.deck}'

from card import Card
from random import shuffle
import requests
import sys
import json

class Deck() :
    def __init__(self, num_decks=1) : 
        self.deck_id = ""
        try:
            decks = requests.get(f"https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count={str(num_decks)}")
            decks.raise_for_status()
            decks = decks.json()
            self.deck_id = decks['deck_id']
        except Exception as e:
            sys.exit(e)

    def __str__(self) :
        return f'Deck_ID: {self.deck_id}'

    def get_card(self) :
        try:       
            FACE_CARDS = {'KING':13, 'QUEEN':12, 'JACK':11, 'ACE':1}
            draw = requests.get(f"https://deckofcardsapi.com/api/deck/{self.deck_id}/draw?count=1")
            draw.raise_for_status()
            cards = draw.json()["cards"]

            for card in cards:
                if card['value'] in FACE_CARDS.keys(): 
                    value = FACE_CARDS[card["value"]]
                else:
                    value = int(card["value"])

                return Card(card['suit'],value)

        except Exception as e:
            sys.exit(e)
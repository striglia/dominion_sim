import random

import cards

class Deck(object):
    
    """
    The Deck class is responsible for holding current information about a
    player's deck and exposing the relvant methods for adding, removing and
    drawing cards from it.

    The relevant variables are:
        draw_pile - the shuffled deck to draw from
        hand - the current cards in hand
        discard_pile - the discarded cards which will be shuffled into draw
        trash_pile - destroyed cards that are removed from the game
        action_coins - count of how many coins are available from actions this turn

    Convention will be that the 0th element of a list is the "top", where
    this is a meaningful distinction.
    """

    # Default constants for the game
    HAND_SIZE = 5

    def __init__(self):
        """Initializes the default deck (3 estate, 7 copper)."""
        self.draw_pile = []
        self.hand = []
        self.discard_pile = []
        self.trash_pile = []
        self.action_coins = 0

        self.init_draw_pile(cards.STARTING_DECK)

        self.draw(self.HAND_SIZE)

    def init_draw_pile(self, cards):
        """Initialize the draw pile with the passed dict of card counts."""
        for card, count in cards.items():
            for _ in range(count):
                self.draw_pile.append(card)
        # And reshuffle for randomness
        random.shuffle(self.draw_pile)

    def draw(self, num):
        """Draws the num cards from the draw pile into hand.
        
        Throws an exception if asked to draw more cards than are available.
        """
        if num < 0:
            raise DrawingNegativeCardsException

        for _ in range(num):
            card = self.draw_one()
            self.hand.append(card)
    
    def draw_one(self):
        """Handles drawing a single card from the deck, shuffling if needed."""
        if len(self.draw_pile) + len(self.discard_pile) == 0:
            raise DrawingWithNoCardsException
        if len(self.draw_pile) == 0:
            self.reshuffle_discard()
        return self.draw_pile.pop(0)

    def reshuffle_discard(self):
        """Reshuffles the discard pile into the draw pile."""
        self.draw_pile = self.discard_pile[:]
        self.discard_pile = []
        random.shuffle(self.draw_pile)

"""
These are here so we can have meaningful exception names.
"""
class DrawingNegativeCardsException(Exception):
    pass

class DrawingWithNoCardsException(Exception):
    pass

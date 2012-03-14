import itertools
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

    Convention will be that the 0th element of a list is the "top", where
    this is a meaningful distinction. These are internally stored as lists,
    since we actually care about order at this level.
    """

    # Default constants for the game
    HAND_SIZE = 5

    def __init__(self, deck=cards.STARTING_DECK):
        """Initializes the default deck (3 estate, 7 copper).
        
        Note this does not draw the initial hand.
        """

        # Turn level variables for # of buys, # of actions and amount of treasure.
        # Note that these all get rewritten and modified by the hand and played
        # cards.
        self.buys = 0
        self.actions = 0
        self.treasure = 0

        self.draw_pile = []
        self.hand = []
        self.discard_pile = []
        self.trash_pile = []
        self.bought_pile = []

        self.init_draw_pile(deck)

    def init_draw_pile(self, cards):
        """Initialize the draw pile with the passed dict of card counts."""
        for card, count in cards.items():
            for _ in range(count):
                self.draw_pile.append(card)
        # And reshuffle for randomness
        random.shuffle(self.draw_pile)

    def draw(self, num):
        """Draws the num cards from the draw pile into hand and updates vars.
        
        Throws an exception if asked to draw more cards than are available.
        """
        if num < 0:
            raise DrawingNegativeCardsException

        for _ in range(num):
            card = self._draw_one()
            self.hand.append(card)
        self._update_deck_vars()
    
    def _draw_one(self):
        """Handles drawing a single card from the deck, shuffling if needed."""
        if len(self.draw_pile) + len(self.discard_pile) == 0:
            raise DrawingWithNoCardsException
        if len(self.draw_pile) == 0:
            self.reshuffle_discard()
        return self.draw_pile.pop(0)

    def _update_deck_vars(self):
        """Uses the current hand and played cards to recalculate variables."""
        self.buys = 1
        self.actions = 1
        self.treasure = 0
        for card in self.hand:
            self.treasure += card.plus_treasure

    def _can_buy(self, card):
        """Tests whether the current hand has enough treasure and buys to buy a card."""
        return (self.treasure >= card.price
                and self.buys >= 1)

    def buy_card(self, card, game):
        """Buys a card from the bank.
        
        Responsible for the following actions:
            - check if the card can be bought (buys and treasure)
            - check if the card exists in the bank
            if so,
            - decrement bank supply
            - reduce buys and treasure appropriately
            - add card to discard pile
        """
        if self._can_buy(card) and game._can_buy(card):
            game.buy_card(card)
            self.treasure -= card.price
            self.buys -= 1
            self.discard_pile.append(card)
        else:
            raise CannotBuyException

    def _can_action(self, card):
        """Tests whether the current hand has enough actions and play an action card."""
        return self.actions >= 1

    def play_action(self, card):
        """Plays an action card from the player's hand.
        
        Responsible for the following actions:
            - check if the card can be played (available actions)
            - check if the card exists in the hand
            if so,
            - transfer card from hand to played_pile
            - add actions/buys/treasure as appropriate
        """
        # Check if we have enough actions and this card is in our hand
        if self.can_action(card) and card in self.hand:
            # Remove an action for playing this card
            self.actions -= 1
            
            # Add any actions, treasure, buys and/or cards
            self.buys += card.plus_buys_on_play
            self.actions += card.plus_actions_on_play
            self.treasure += card.plus_treasure_on_play
            self.draw(card.plus_cards_on_play)

            # Move card from hand to played_pile
            self._play_card_from_hand(card)
        else:
            raise CannotActionException

        return self.actions >= 1

    def _play_card_from_hand(self, card):
        """Take card from the hand and transfer to played_pile. DO NOT trigger
        any of the cards effects."""
        self.hand.remove(card)
        self.played_pile.append(card)

    def reshuffle_discard(self):
        """Reshuffles the discard pile into the draw pile."""
        self.draw_pile = self.discard_pile[:]
        self.discard_pile = []
        random.shuffle(self.draw_pile)

    def calc_total_vp(self):
        """Calculates total VP in all piles (for end game)."""
        total_vp = 0
        for card in itertools.chain(self.hand, self.discard_pile, self.draw_pile):
            total_vp += card.vp()
        return total_vp

"""
These are here so we can have meaningful exception names.
No actual functionality aside from the names.
"""
class DrawingNegativeCardsException(Exception):
    pass

class DrawingWithNoCardsException(Exception):
    pass

class CannotBuyException(Exception):
    pass

class CannotActionException(Exception):
    pass

import itertools
import random

class CardNotInHandError(Exception):
    """Raised when a player attemps to play a card he doesn't have in hand."""
    pass

class NoActionsAvailable(Exception):
    """Raised when a player attemps to play a card without an action available."""
    pass

class NotActionCardError(Exception):
    """Raised when a player attemps to play a card that isn't an Action card."""
    pass


class Deck(object):
    """
    Class for reprensenting a player's deck.
    """

    # Module-level constants
    HAND_SIZE = 5

    def __init__(self, cards):
        self.draw = list(cards)
        self.hand = []
        self.discard = []
        self.played = []

        self.actions = 1
        self.buys = 1
        self.treasure = 0

        # Draw first hand
        self.draw_cards(self.HAND_SIZE)

    def _draw_one_card(self):
        """Draws one card into the hand."""
        # If draw is empty, shuffle in the discard pile
        if not self.draw:
            if not self.discard:
                # If there are no draw or discard cards left, do a no-op
                return
            self.draw = list(self.discard)
            random.shuffle(self.draw)
            self.discard = []
        self.hand.append(self.draw.pop())

    def draw_cards(self, num):
        """Draws num cards from the draw pile and places them in the hand."""
        for _ in range(num):
            self._draw_one_card()

    def play_action(self, card):
        """Attempts to play the card from this deck's hand."""
        if card not in self.hand:
            raise CardNotInHandError
        if not card.is_action:
            raise NotActionCardError
        if self.actions < 1:
            raise NoActionsAvailableError

        self.hand.remove(card)
        self.played.append(card)
        self.actions -= 1
        self.actions += card.plus_actions
        self.buys += card.plus_buys
        self.treasure += card.plus_treasure

        self.draw_cards(card.plus_cards)

    def count_vp(self):
        """Counts the total VP in the Deck."""
        return sum(c.vp for c in itertools.chain(self.hand, self.draw, self.discard))

    def count_treasure(self):
        """Counts the treasure in hand."""
        return sum(c.treasure for c in self.hand)

from deck import Deck
import cards

class Player(object):

    """
    The player class is responsible for simulating a single player,
    including their current deck and hand and their strategy.
    """

    def __init__(self, deck):
        """Set up a default strategy, initialize the player's deck and hand."""
        self.deck = Deck(deck)

    def play_one_turn(self, game):
        raise NotImplementedError

class MockPlayer(Player):
    
    """
    Testing player. Just illegally buys a province every turn to ensure the
    game will eventually end.
    """

    def play_one_turn(self, game):
        # TODO: Make this use proper helpers rather than directly modify shit
        game.banked_cards[cards.Province] -= 1
        self.deck.discard_pile.append(cards.Province)

from game import Game
from deck import Deck
from utility import deck_has_cards
from utility import cards_are_same
import cards

from testify import TestCase
from testify import assert_equal
from testify import assert_raises

class GameTestCase(TestCase):
    """Tests out the various game-level behaviors."""

    def test_initialization(self):
        game = Game()

        # Ensure that default game is default
        assert(deck_has_cards(game.p1.deck, cards.STARTING_DECK))
        assert(deck_has_cards(game.p2.deck, cards.STARTING_DECK))
        assert(cards_are_same(game.banked_cards, cards.CARD_SETS['trivial']))

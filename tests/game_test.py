from game import Game
from deck import Deck
from player import MockPlayer
from utility import cards_are_same
from utility import deck_has_cards
import cards

from testify import TestCase
from testify import assert_equal
from testify import assert_raises

class GameTestCase(TestCase):
    """Tests out the various game-level behaviors."""

    def test_initialization(self):
        """Test that both players' decks and the bank are initialized properly."""
        game = Game()

        # Ensure that default game is default
        assert(deck_has_cards(game.p1.deck, cards.STARTING_DECK))
        assert(deck_has_cards(game.p2.deck, cards.STARTING_DECK))
        assert(cards_are_same(game.banked_cards, cards.CARD_SETS['trivial']))

    def test_basic_game(self):
        """Tests that a game can be played without exceptions or errors."""
        game = Game(p1_class=MockPlayer, p2_class=MockPlayer)
        game.play_one_game()

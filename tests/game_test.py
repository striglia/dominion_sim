from game import Game
from deck import Deck
from player import MockProvince
from player import Mock3Stack
from player import Moron
from player import Money
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
        # Test with province end condition
        game = Game(p1_class=MockProvince, p2_class=MockProvince)
        game.play_one_game()

        # Test with three stacks empty end condition
        game = Game(p1_class=Mock3Stack, p2_class=Mock3Stack)
        game.play_one_game()

    def test_moron_vs_money(self):
        """Test that Money beats Moron."""
        #TODO: Make repeatedly testing games cleaner.
        for _ in range(100):
            game = Game(p1_class=Moron, p2_class=Money)
            winner = game.play_one_game()
            assert_equal(winner, 2)

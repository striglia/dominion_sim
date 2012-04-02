from dingus import Dingus
from unittest import main
from unittest import TestCase

from deck import Deck
from deck import CardNotInHandError
from deck import NotActionCardError

def fill_with_n(n):
    """Helper method that returns n arbitrary cards.""" 
    return [StubCard for _ in range(n)]

class BaseDeckTestCase(TestCase):
    """Basic test case with setup."""

    def setUp(self, starting_cards=[]):
        """Initializes all parts of the deck."""
        self.deck = Deck(starting_cards)

class StubCard(object):
    """Fake card object with default values so we can be independent from the cards module."""

    is_action = True
    cost = 8
    vp = 6
    treasure = 0

    # On action bonuses
    plus_actions = 1
    plus_cards = 1
    plus_buys = 1
    plus_treasure = 1


class DeckDrawTestCase(BaseDeckTestCase):
    """Tests out drawing from a Deck."""

    def test_draw_n(self):
        """Tests that we can draw N from the draw_pile correctly."""
        num_to_draw = 5

        # Set hand to be empty and draw to have num_to_draw cards
        self.deck.draw = fill_with_n(num_to_draw)
        self.deck.hand = []
        self.deck.draw_cards(num=num_to_draw)
        assert len(self.deck.draw) == 0
        assert len(self.deck.hand) == num_to_draw

    def test_draw_into_discard(self):
        """Test we fall back to the discard pile and it gets shuffled into draw."""
        num_to_draw = 5

        self.deck.draw = fill_with_n(num_to_draw - 1)
        self.deck.hand = []
        self.deck.discard = fill_with_n(num_to_draw)
        self.deck.draw_cards(num=num_to_draw)
        assert len(self.deck.discard) == 0
        assert len(self.deck.draw) == num_to_draw - 1
        assert len(self.deck.hand) == num_to_draw

class DeckSummaryTestCase(BaseDeckTestCase):
    """Tests out the summarization of a player's Deck."""

    def test_count_hand_vp(self):
        vp_vals = [1, 2, 3]
        self.deck.hand = [Dingus(vp=val) for val in vp_vals]
        assert self.deck.count_vp() == sum(vp_vals)

    def test_count_hand_treasure(self):
        treasure_vals = [1, 2, 3]
        self.deck.hand = [Dingus(treasure=val) for val in treasure_vals]
        assert self.deck.count_treasure() == sum(treasure_vals)

    def test_illegal_plays(self):
        """Check for various exceptions when playing illegal actions."""
        fake_card = Dingus(is_action=False)
        self.deck.hand = [fake_card]
        self.assertRaises(CardNotInHandError, self.deck.play_action, Dingus())
        self.assertRaises(NotActionCardError, self.deck.play_action, fake_card)

    def test_plus_actions(self):
        draw_card = Dingus()
        hand_card = StubCard()
        self.deck.draw = [draw_card]
        self.deck.hand = [hand_card]
        self.deck.played = []

        # Check that we added an action, buy, treasure and card.
        self.deck.play_action(hand_card)
        assert self.deck.draw == []
        assert self.deck.hand == [draw_card]
        assert self.deck.played == [hand_card]
        assert self.deck.actions == 1
        assert self.deck.buys == 2
        assert self.deck.treasure == 1

class DeckInitializeTestCase(BaseDeckTestCase):
    """Tests out the initial state of a Deck."""

    def test_initialize_deck(self):
        """Tests that the deck starts with a full hand."""
        cards = [StubCard for _ in range(Deck.HAND_SIZE)]
        deck = Deck(cards)
        # Relies on setUp doing the right thing
        assert len(deck.hand) == deck.HAND_SIZE

class DeckBuyTestCase(BaseDeckTestCase):
    """Tests out purchasing cards with the current hand."""

    def test_can_purchase(self):
        """Tests the check for whether a card can be purchased."""
        cards = [StubCard for _ in range(Deck.HAND_SIZE)]
        deck = Deck(cards)
        # Relies on setUp doing the right thing
        assert len(deck.hand) == deck.HAND_SIZE

if __name__ == '__main__':
    main()

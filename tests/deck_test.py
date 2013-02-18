from testify import TestCase
from testify import setup
from testify import assert_equal
from testify import assert_raises
from testify import run
from deck import Deck
from deck import DrawingNegativeCardsException
from deck import DrawingWithNoCardsException
from utility import cards_are_same
import cards

class DeckTestCase(TestCase):
    """Tests out the various deck-related methods and edge cases."""

    @setup
    def build_deck(self):
        self.deck = Deck()

    def test_starting_cards(self):
        """Test that the starting hand+draw contains the correct cards."""
        all_cards = self.deck.hand
        all_cards.extend(self.deck.draw_pile)

        assert_equal(cards_are_same(all_cards, cards.STARTING_DECK), True)

    def test_random_ordering(self):
        """Test that the actual ordering of the initial hand is randomized.

        Note that this is technically a flaky test, since we could draw
        repeated random hands and have them all be identical. But odds are
        overwhelmingly in our favor.
        """
        # The odds of getting 10 identical hands with shuffling is....low
        num_tries = 10
        attempt = 0

        while attempt < num_tries:
            attempt += 1
            deck_alt = Deck()
            if not cards_are_same(self.deck.hand, deck_alt.hand):
                raise AssertionError('Cards were non-identical!')

    def test_draw_negative_cards(self):
        """Tests drawing -1 cards throws an exception."""
        assert_raises(DrawingNegativeCardsException, self.deck.draw, -1)

    def test_draw_no_cards(self):
        """Tests drawing no cards does not affect piles."""
        old_hand_size = len(self.deck.hand)
        old_draw_size = len(self.deck.draw_pile)
        old_discard_size = len(self.deck.discard_pile)
        self.deck.draw(0)
        assert_equal(len(self.deck.hand), old_hand_size)
        assert_equal(len(self.deck.draw_pile), old_draw_size)
        assert_equal(len(self.deck.discard_pile), old_discard_size)

    def test_draw_all_cards(self):
        """Tests drawing all card empties non-hand piles."""
        old_hand_size = len(self.deck.hand)
        old_draw_size = len(self.deck.draw_pile)
        old_discard_size = len(self.deck.discard_pile)
        self.deck.draw(old_draw_size + old_discard_size)
        assert_equal(len(self.deck.hand), old_hand_size + old_draw_size + old_discard_size)
        assert_equal(len(self.deck.draw_pile), 0)
        assert_equal(len(self.deck.discard_pile), 0)

    def test_draw_too_many_cards(self):
        """Test that drawing too many cards throws the relevant exception."""
        assert_raises(DrawingWithNoCardsException, self.deck.draw, 99)

    def test_draw(self):
        """Test that we can draw more than are in the draw pile without error."""
        self.deck.discard_pile = self.deck.draw_pile[:]

        # Save original sizes
        hand_original_size = len(self.deck.hand)
        discard_pile_original_size = len(self.deck.discard_pile)
        total_num_cards = len(self.deck.hand) + len(self.deck.draw_pile) + len(self.deck.discard_pile)

        # We will draw one more card than the draw pile contains
        draw_num = len(self.deck.draw_pile) + 1

        self.deck.draw(draw_num)

        # Assert all the various piles are the proper size
        assert_equal(len(self.deck.discard_pile), 0)
        assert_equal(len(self.deck.draw_pile), discard_pile_original_size - 1)
        assert_equal(len(self.deck.hand), hand_original_size + draw_num)
        assert_equal(len(self.deck.hand)
                + len(self.deck.draw_pile)
                + len(self.deck.discard_pile), total_num_cards)

class DeckHelpersTestCase(TestCase):
    """Tests out the various deck-related helper methods."""

    def test_can_buy(self):
        """Test out the _can_buy helper method."""
        deck = Deck()
        deck.treasure = 3
        deck.buys = 1

        # Test too little treasure for the card
        assert_equal(deck._can_buy(cards.Gold), False)
        # Test just enough
        assert_equal(deck._can_buy(cards.Silver), True)
        # Test too much
        assert_equal(deck._can_buy(cards.Copper), True)

    def test_calc_total_vp(self):
        """Test calculating the total vp in a player's deck."""
        deck = Deck()

        # Test that a default deck has 3 VP
        assert_equal(deck.calc_total_vp(), 3)

        # Test that adding a province gives 9 VP
        deck.discard_pile.append(cards.Province)
        assert_equal(deck.calc_total_vp(), 9)


if __name__ == '__main__':
    run()

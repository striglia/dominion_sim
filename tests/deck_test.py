from testify import TestCase
from testify import assert_equal
from testify import assert_raises
from deck import Deck
from deck import DrawingNegativeCardsException
from deck import DrawingWithNoCardsException
from utility import cards_are_same
import cards

class DeckTestCase(TestCase):
    """Tests out the various deck-related methods and edge cases."""

    def test_hand_initialization(self):
        """Test that the starting hand is random and starting deck is right.
        
        Note that this is technically a flaky test, since we could draw
        repeated random hands and have them all be identical. But odds are
        overwhelmingly in our favor.
        """
        deck = Deck()
        all_cards = deck.hand
        all_cards.extend(deck.draw_pile)

        assert_equal(cards_are_same(all_cards, cards.STARTING_DECK), True)

        # The odds of getting 10 identical hands with shuffling is....low
        num_tries = 10 
        attempt = 0
        same_hand = True

        while same_hand and attempt < num_tries:
            deck_alt = Deck()
            same_hand = cards_are_same(deck.hand, deck_alt.hand)
        assert_equal(same_hand, False)

    def test_draw_edge_amounts(self):
        """Tests drawing -1 cards, 0 cards, all cards remaining, too many cards.

        Drawing -1 and too many should throw exceptions. Tests that all card
        piles are the right size otherwise.
        """
        deck = Deck()
        assert_raises(DrawingNegativeCardsException, deck.draw, -1)

        deck = Deck() # reset deck
        old_hand_size = len(deck.hand)
        old_draw_size = len(deck.draw_pile)
        old_discard_size = len(deck.discard_pile)
        deck.draw(0)
        assert_equal(len(deck.hand), old_hand_size)
        assert_equal(len(deck.draw_pile), old_draw_size)
        assert_equal(len(deck.discard_pile), old_discard_size)

        deck = Deck() # reset deck
        old_hand_size = len(deck.hand)
        old_draw_size = len(deck.draw_pile)
        old_discard_size = len(deck.discard_pile)
        deck.draw(old_draw_size + old_discard_size)
        assert_equal(len(deck.hand), old_hand_size + old_draw_size + old_discard_size)
        assert_equal(len(deck.draw_pile), 0)
        assert_equal(len(deck.discard_pile), 0)

        deck = Deck() # reset deck
        assert_raises(DrawingWithNoCardsException, deck.draw, 99)

    def test_draw(self):
        """Test that we can draw more than are in the draw pile without error."""
        deck = Deck()
        deck.discard_pile = deck.draw_pile[:]

        # Save original sizes
        draw_pile_original_size = len(deck.draw_pile)
        hand_original_size = len(deck.hand)
        discard_pile_original_size = len(deck.discard_pile)
        total_num_cards = len(deck.hand) + len(deck.draw_pile) + len(deck.discard_pile)

        # We will draw one more card than the draw pile contains 
        draw_num = len(deck.draw_pile) + 1

        deck.draw(draw_num)
        
        # Assert all the various piles are the proper size
        assert_equal(len(deck.discard_pile), 0)
        assert_equal(len(deck.draw_pile), discard_pile_original_size - 1)
        assert_equal(len(deck.hand), hand_original_size + draw_num)
        assert_equal(len(deck.hand) 
                + len(deck.draw_pile) 
                + len(deck.discard_pile), total_num_cards)

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

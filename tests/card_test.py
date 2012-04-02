from flexmock import flexmock
from unittest import TestCase
from unittest import main
import inspect

import cards

def verify_card(card):
    """Verifies that the Card subclass passed is acceptable."""
    rules = [
            getattr(card, 'is_implemented', True),
            card.cost > -1,
            card.vp is not None,
            card.treasure > -1,
            card.plus_actions > -1,
            card.plus_cards > -1,
            card.plus_buys > -1,
            card.plus_treasure > -1,
            ]
    return all(rules)

class CardTestCase(TestCase):
    """Tests out the validity of the cards defined in cards.py"""

    def test_all_cards_are_valid(self):
        """Walks through every card defined in cards.py and tests to make
        sure all necessary fields are present and all fields are valid."""
        # Walk through all defined sub-classes of Card in cards.py
        for card_name, card_obj in inspect.getmembers(cards):
            # If it is an implemented card, verify it has acceptable fields
            if (type(card_obj) is type 
                    and any([base == cards.Card for base in card_obj.__bases__])):
                assert verify_card(card_obj) == True

if __name__ == '__main__':
    main()

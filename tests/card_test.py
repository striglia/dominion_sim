from testify import *
import cards

import inspect

def verify_card(card):
    """Verifies that the Card subclass passed is acceptable."""
    rules = [
        card.price >= 0,
        card.plus_cards_on_play >= 0,
        card.plus_buys_on_play >= 0,
        card.plus_actions_on_play >= 0,
        card.plus_treasure >= 0,
        card.plus_treasure_on_play >= 0,
        not card.is_action or 'on_action' not in card.__dict__,
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
                    and any([base == cards.Card for base in card_obj.__bases__])
                    and getattr(card_obj, 'is_implemented', True)):
                assert_equal(verify_card(card_obj), True)

if __name__=='__main__':
    run()

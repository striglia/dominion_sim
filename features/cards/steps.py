from lettuce import step
from lettuce import world

import cards

@step("I am considering the (\w+) card")
def considering_x_card(self, card_name):
    world.card = getattr(cards, card_name)

@step("Validate the card's values")
def validate_card_values(self):
    rules = [
            getattr(world.card, 'is_implemented', True),
            world.card.cost > -1,
            world.card.vp is not None,
            world.card.treasure > -1,
            world.card.plus_actions > -1,
            world.card.plus_cards > -1,
            world.card.plus_buys > -1,
            world.card.plus_treasure > -1,
            ]
    assert all(rules)


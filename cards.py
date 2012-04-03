class Card(object):

    """
    Base class for all card classes.

    Defines default values for basic card properties.
    """

class Province(Card):
    is_action = False
    cost = 8
    vp = 6
    treasure = 0

    # On action bonuses
    plus_actions = 0
    plus_cards = 0
    plus_buys = 0
    plus_treasure = 0

class Duchy(Card):
    is_action = False
    cost = 5
    vp = 3
    treasure = 0

    # On action bonuses
    plus_actions = 0
    plus_cards = 0
    plus_buys = 0
    plus_treasure = 0

class Estate(Card):
    is_action = False
    cost = 2
    vp = 1
    treasure = 0

    # On action bonuses
    plus_actions = 0
    plus_cards = 0
    plus_buys = 0
    plus_treasure = 0

class Curse(Card):
    is_action = False
    cost = 0
    vp = -1
    treasure = 0

    # On action bonuses
    plus_actions = 0
    plus_cards = 0
    plus_buys = 0
    plus_treasure = 0

class Gold(Card):
    is_action = False
    cost = 6
    vp = 0
    treasure = 3

    # On action bonuses
    plus_actions = 0
    plus_cards = 0
    plus_buys = 0
    plus_treasure = 0

class Silver(Card):
    is_action = False
    cost = 3
    vp = 0
    treasure = 2

    # On action bonuses
    plus_actions = 0
    plus_cards = 0
    plus_buys = 0
    plus_treasure = 0

class Copper(Card):
    is_action = False
    cost = 0
    vp = 0
    treasure = 1

    # On action bonuses
    plus_actions = 0
    plus_cards = 0
    plus_buys = 0
    plus_treasure = 0

class Villiage(Card):
    is_action = True
    cost = 3
    vp = 0
    treasure = 0
    
    # On action bonuses
    plus_actions = 2
    plus_cards = 1
    plus_buys = 0
    plus_treasure = 0

class Smithy(Card):
    is_action = True
    cost = 4
    vp = 0
    treasure = 0

    # On action bonuses
    plus_actions = 0
    plus_cards = 2
    plus_buys = 0
    plus_treasure = 0

class Laboratory(Card):
    is_action = True
    cost = 5
    vp = 0
    treasure = 0

    # On action bonuses
    plus_actions = 1
    plus_cards = 2
    plus_buys = 0
    plus_treasure = 0

class Market(Card):
    is_action = True
    cost = 5
    vp = 0
    treasure = 0

    # On action bonuses
    plus_actions = 1
    plus_cards = 1
    plus_buys = 1
    plus_treasure = 1

class Woodcutter(Card):
    is_action = True
    cost = 3
    vp = 0
    treasure = 0

    # On action bonuses
    plus_actions = 0
    plus_cards = 0
    plus_buys = 1
    plus_treasure = 2

starting_cards = [Estate, Estate, Estate, Copper, Copper,
        Copper, Copper, Copper, Copper, Copper]
trivial_deck = {
        Province: 8,
        Duchy: 8,
        Estate: 8,
        Gold: 8,
        Silver: 8,
        Copper: 8}

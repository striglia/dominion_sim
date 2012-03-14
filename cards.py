class Card(object):
    """
    Base class for all cards in the simulator. Holds card type, price, vp, actions.

    Defaults to reasonable values so later classes can look more like their
    card in Dominion.
    REQUIRED VARIABLES:
    name - name of this card. Capitalized.
    price - price of this card in coins

    plus_cards_on_play - number of cards playing this adds (is_action should be True)
    plus_actions_on_play - number of actions playing this adds (is_action should be True) 
    plus_buys_on_play - number of buys playing this adds (is_action should be True)
    plus_treasure_on_play - number of coins playing this adds

    plus_treasure - number of coins holding this adds
    plus_card_on_buy - a card (or None) you get upon purchase of this card
    """
    is_action = False
    is_treasure = False
    is_vp = False

    plus_cards_on_play = 0
    plus_actions_on_play = 0
    plus_buys_on_play = 0
    plus_treasure_on_play = 0

    plus_treasure = 0
    plus_card_on_buy = None

    """
    REQUIRED METHODS:
    on_purchase - accepts a Game object and mutates both players's decks as needed.
        Note that this should only be used to implement effects written on the card!
    on_action - accepts a Game object and mutates both players's decks as needed
        Note that this should only be used to implement effects written on the card!
    vp - amount of vp this provides. Takes the current Deck object as an argument.
    """
    def on_purchase(self, game):
        pass
    def on_action(self, game):
        pass
    @staticmethod
    def vp():
        return 0

"""Base Victory and Money cards."""
class Province(Card):
    name = 'Province'
    price = 8
    is_vp = True

    @staticmethod
    def vp():
        return 6

class Duchy(Card):
    name = 'Duchy'
    price = 5
    is_vp = True
 
    @staticmethod
    def vp():
        return 3

class Estate(Card):
    name = 'Estate'
    price = 2
    is_vp = True

    @staticmethod
    def vp():
        return 1

class Curse(Card):
    name = 'Curse'
    price = 0
    is_vp = True

    @staticmethod
    def vp():
        return -1

class Gold(Card):
    name = 'Gold'
    price = 6
    is_treasure = True
    plus_treasure = 3

class Silver(Card):
    name = 'Silver'
    price = 3
    is_treasure = True
    plus_treasure = 2

class Copper(Card):
    name = 'Copper'
    price = 0
    is_treasure = True
    plus_treasure = 1

"""Base set cards."""
class Adventurer(Card):
    name = 'Adventurer'
    price = 6
    is_action = True
    # No idea how to do conditional drawing yet =(
    is_implemented = False

class Bureaucrat(Card):
    name = 'Bureaucrat'
    price = 4
    is_action = True
    # No idea how to do so much here
    is_implemented = False

class Chancellor(Card):
    name = 'Chancellor'
    price = 3
    is_action = True
    plus_treasure = 2
    is_implemented = False

class Cellar(Card):
    name = 'Cellar'
    price = 2
    is_action = True
    plus_actions = 1
    # No idea how to do conditional discarding yet =(
    is_implemented = False

class Chapel(Card):
    name = 'Chapel'
    price = 2
    is_action = True
    # Conditional discard
    is_implemented = False

class CouncilRoom(Card):
    name = 'Council Room'
    is_action = True
    is_implemented = False

class Feast(Card):
    name = 'Feast'
    is_action = True
    is_implemented = False

class Festival(Card):
    name = 'Festival'
    price = 5
    plus_treasure_on_play = 2
    plus_actions_on_play = 2
    plus_buys_on_play = 1
    is_action = True
    is_implemented = False

class Gardens(Card):
    name = 'Gardens'
    is_vp = True
    is_implemented = False

class Laboratory(Card):
    name = 'Laboratory'
    price = 5
    plus_actions_on_play = 1
    plus_cards_on_play = 2
    is_action = True

class Library(Card):
    name = 'Library'
    is_implemented = False

class Market(Card):
    name = 'Market'
    price = 5
    plus_actions_on_play = 1
    plus_cards_on_play = 1
    plus_buys_on_play = 1
    plus_treasure_on_play = 1
    is_action = True

class Militia(Card):
    name = 'Militia'
    is_action = True
    is_implemented = False

class Mine(Card):
    name = 'Mine'
    is_action = True
    is_implemented = False

class Moat(Card):
    name = 'Moat'
    is_action = True
    is_implemented = False

class Moneylender(Card):
    name = 'Moneylender'
    is_action = True
    is_implemented = False

class Remodel(Card):
    name = 'Remodel'
    is_action = True
    is_implemented = False

class Smithy(Card):
    name = 'Smithy'
    price = 4
    plus_actions_on_play = 3
    is_action = True

class Spy(Card):
    name = 'Spy'
    is_action = True
    is_implemented = False

class Thief(Card):
    name = 'Thief'
    is_action = True
    is_implemented = False

class ThroneRoom(Card):
    name = 'ThroneRoom'
    is_action = True
    is_implemented = False

class Village(Card):
    name = 'Village'
    price = 3
    plus_card_on_play = 1
    plus_actions_on_play = 2
    is_action = True

class Witch(Card):
    name = 'Witch'
    is_action = True
    is_implemented = False

class Woodcutter(Card):
    name = 'Woodcutter'
    price = 3
    plus_treasure_on_play = 2
    plus_buys_on_play = 1
    is_action = True

class Workshop(Card):
    name = 'Workshop'
    is_action = True
    is_implemented = False


STARTING_DECK = {Estate: 3, Copper: 7}
CARD_SETS = {
        'trivial': {
            Province: 8,
            Duchy: 8,
            Estate: 8,
            Gold: 30,
            Silver: 40,
            Copper: 60,
            }
        }

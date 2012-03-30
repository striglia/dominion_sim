from deck import Deck
import cards

class Player(object):

    """
    The player class is responsible for simulating a single player,
    including their current deck and hand and their strategy.
    """

    def __init__(self, deck):
        """Set up a default strategy, initialize the player's deck and hand."""
        self.deck = Deck(deck)

    def can_buy(self, card):
        """Convenience method for self.deck._can_buy(card)."""
        return self.deck._can_buy(card)

    def buy_card(self, card, game):
        """Convenience method for self.deck.buy_card(card, game)."""
        self.deck.buy_card(card, game)

    def new_hand(self):
        """Empties current hand into discard, redraws new hand."""
        self.deck.discard_pile.extend(self.deck.hand)
        self.deck.hand = []
        self.deck.draw(self.deck.HAND_SIZE)
        self.deck._update_deck_vars()

    def num_in_bank(self, card, game):
        """Returns the number of this card left in the bank."""
        return game.num_in_bank(card)

    def play_one_turn(self, game):
        raise NotImplementedError

class Moron(Player):

    """
    The most trivial player who only buys Gold, Silver and Copper (in this order).
    """

    def play_one_turn(self, game):
        """Buy a single Gold, Silver and Copper, in this order, every turn."""
        if self.can_buy(cards.Gold):
            self.buy_card(cards.Gold, game)
        elif self.can_buy(cards.Silver):
            self.buy_card(cards.Silver, game)
        elif self.can_buy(cards.Copper):
            self.buy_card(cards.Copper, game)

class Money(Player):

    """
    The second most trivial player.
    Buys Provinces, Gold, Silver, in this order, every turn.
    """

    def play_one_turn(self, game):
        """Buys Provinces, Gold, Silver, in this order, every turn."""
        if self.can_buy(cards.Province):
            self.buy_card(cards.Province, game)
        if self.can_buy(cards.Gold):
            self.buy_card(cards.Gold, game)
        elif self.can_buy(cards.Silver):
            self.buy_card(cards.Silver, game)

class BigMoney(Player):

    """
    Obeys these rules, in order:
        - Province: always
        - Duchy: <= d provinces left in bank
        - Estate: <= e provinces left in bank
        - Gold: always
        - Silver: always
    """

    # Hyperparameters set by fiat (for now)
    d = 5
    e = 2

    def play_one_turn(self, game):
        """Buys cards in this order."""
        if self.can_buy(cards.Province):
            self.buy_card(cards.Province, game)
        elif self.num_in_bank(cards.Province, game) < self.d and self.can_buy(cards.Duchy):
            self.buy_card(cards.Duchy, game)
        elif self.num_in_bank(cards.Province, game) < self.d and self.can_buy(cards.Estate):
            self.buy_card(cards.Estate, game)
        elif self.can_buy(cards.Gold):
            self.buy_card(cards.Gold, game)
        elif self.can_buy(cards.Silver):
            self.buy_card(cards.Silver, game)

class MockProvince(Player):
    
    """
    Testing player. Just illegally buys a province every turn to ensure the
    game will eventually end.
    """

    def play_one_turn(self, game):
        # TODO: Make this use proper helpers rather than directly modify shit
        game.banked_cards[cards.Province] -= 1
        self.deck.discard_pile.append(cards.Province)

class Mock3Stack(Player):
    
    """
    Testing player. Just illegally buys a copper+silver+gold each turn to ensure the
    game will eventually end.
    """

    def play_one_turn(self, game):
        # TODO: Make this use proper helpers rather than directly modify shit
        game.banked_cards[cards.Gold] -= 1
        game.banked_cards[cards.Silver] -= 1
        game.banked_cards[cards.Copper] -= 1
        self.deck.discard_pile.append(cards.Gold)
        self.deck.discard_pile.append(cards.Silver)
        self.deck.discard_pile.append(cards.Copper)

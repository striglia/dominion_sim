import copy

import cards
from player import Player

class Game(object):

    """
    The main class which governs a single game of Dominion.
    """

    def __init__(self, deck=None, p1_class=Player, p2_class=Player):
        """Initializes the bank, players and cards."""
        #XXX: Currently defaults to playing with VP and Money only.
        self.card_set = 'trivial'
        self.current_player = 1
        self.banked_cards = copy.deepcopy(cards.CARD_SETS[self.card_set])

        # Variables for game stats
        self.turn_num = 1
        self.winning_player = []
        self.player_vp = []

        initial_deck = deck or cards.STARTING_DECK
        self.p1 = p1_class(initial_deck)
        self.p2 = p2_class(initial_deck)

    def play_one_game(self):
        """Here is the logic required to run through to completion a single game of Dominion.

        The main loop governs the swapping of turns and testing of game completion.
        """
        
        while not self._game_over():
            self.play_one_turn()
            self.collect_stats()
            self.turn_num += 1

        return self.winning_player[-1]

    def play_one_turn(self):
        """The current player plays one turn, as directed by their Player object."""
        #XXX: My laziness knows no bounds. Only allows two players.
        #XXX: I pass the whole game object through to players. Ugh.
        
        if self.current_player == 1:
            self.p1.new_hand()
            self.p1.play_one_turn(self)
            self.current_player = 2
        else:
            self.p2.new_hand()
            self.p2.play_one_turn(self)
            self.current_player = 1

    def collect_stats(self):
        """Calculates useful statistics on this game."""
        #TODO: Make this actually matter
        vp_p1 = self.p1.deck.calc_total_vp()
        vp_p2 = self.p2.deck.calc_total_vp()
        if vp_p1 > vp_p2:
            self.winning_player.append(1)
        elif vp_p1 < vp_p2:
            self.winning_player.append(2)
        else:
            self.winning_player.append(None)
        self.player_vp.append((vp_p1, vp_p2))

    def num_in_bank(self, card):
        """Returns the number of this card in the bank."""
        return self.banked_cards[card]

    def buy_card(self, card):
        """Buys a card from the bank, decrementing the number left."""
        if not self._can_buy(card):
            raise CannotBuyException
        self.banked_cards[card] -= 1

    def _can_buy(self, card):
        """Checks if the card is available from banked_cards."""
        return self.banked_cards[card] > 0

    def _game_over(self):
        """Test if the game is complete."""

        if (self.banked_cards[cards.Province] == 0
                or self._three_stacks_gone()):
            return True
        return False

    def _three_stacks_gone(self):
        """Returns a boolean indicating whether three or more bank stacks are emptied."""
        return sum([1.0 for count in self.banked_cards.values() if count == 0])

class CannotBuyException(Exception):
    pass

import cards
from player import Player

class Game(object):

    """
    The main class which governs a single game of Dominion.
    """

    #XXX: Currently defaults to playing with VP and Money only.
    card_set = 'trivial'

    def __init__(self):
        self.initialize_cards()
        self.current_player = 1

    def initialize_cards(self):
        """Initializes the bank of cards depending on self.card_set."""
        self.banked_cards = cards.CARD_SETS[self.card_set]

        initial_deck = cards.STARTING_DECK
        self.p1 = Player(initial_deck)
        self.p2 = Player(initial_deck)

    def play_one_game(self):
        """Here is the logic required to run through to completion a single game of Dominion.

        The main loop governs the swapping of turns and testing of game completion.
        """
        
        while not self.game_over():
            self.play_one_turn()

        self.collect_stats()
        return self.winning_player

    def play_one_turn(self):
        """The current player plays one turn, as directed by their Player object."""
        #XXX: My laziness knows no bounds. Only allows two players.
        #XXX: I pass the whole game object through to players. Ugh.
        if self.current_player == 1:
            self.p1.play_one_turn(self)
        else:
            self.p2.play_one_turn(self)

    def game_over(self):
        """Test if the game is complete."""

        if (self.banked_cards['Province'] == 0
                or self.three_stacks_gone()):
            return True
        return False

    def three_stacks_gone(self):
        """Returns a boolean indicating whether three or more bank stacks are emptied."""
        return sum([1.0 for count in self.banked_cards.values() if count == 0])

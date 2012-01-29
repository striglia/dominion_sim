class Player(object):

    """
    The player class is responsible for simulating a single player,
    including their current deck and hand and their strategy.
    """

    def __init__(self, deck):
        """Set up a default strategy, initialize the player's deck and hand."""
        self.deck = Deck(deck)

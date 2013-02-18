import collections
import itertools

def cards_are_same(hand1, hand2):
    """Helper that tests that two sets of cards are identical up to ordering.

    As an added bonus, this can handle any combination of card lists
    and card dicts.
    """
    hand1_dict = {}
    hand2_dict = {}

    # List -> Dict conversion
    if isinstance(hand1, dict):
        hand1_dict = hand1
    else:
        for card in hand1:
            hand1_dict[card] = hand1_dict.get(card, 0) + 1
    if isinstance(hand2, dict):
        hand2_dict = hand2
    else:
        for card in hand2:
            hand2_dict[card] = hand2_dict.get(card, 0) + 1

    return hand1_dict == hand2_dict

def deck_has_cards(deck, cards):
    """Helper that tests if a deck is the same as a set of cards.

    Assumes that cards is a dict.
    """
    deck_dict = collections.defaultdict(int)
    for card in itertools.chain(deck.draw_pile, deck.discard_pile, deck.hand):
        deck_dict[card] += 1
    return deck_dict == cards

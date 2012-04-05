from lettuce import step
from lettuce import world
from dingus import Dingus
from nose.tools import assert_raises

from deck import Deck
from deck import ActionError

# Setup

@step('I have a dummy deck')
def have_dummy_deck(self):
    starting_cards = []
    world.deck = Deck(starting_cards)

@step('I have a new deck')
def have_new_deck(self):
    starting_cards = [Dingus('card %d' % i) for i in range(10)]
    world.deck = Deck(starting_cards)

# Setters

@step('My (\w+) has (\d+) cards with (\d+) (\w+)')
def piles_have_cards_with_vp(self, pile, num_cards, num_attr, attr):
    if attr == 'VP':
        setattr(world.deck, pile, [Dingus('fake card %d' % i, vp=int(num_attr)) for i in range(int(num_cards))])
    elif attr == 'treasure':
        setattr(world.deck, pile, [Dingus('fake card %d' % i, treasure=int(num_attr)) for i in range(int(num_cards))])

@step('I have (\d+) buys')
def have_n_buys(self, number):
    world.deck.buys = int(number)

@step('I have (\d+) treasure')
def have_n_treasure(self, number):
    world.deck.treasure = int(number)

@step('I have (\d+) actions')
def have_n_actions(self, num_actions):
    world.deck.actions = int(num_actions)

@step('I have (\d+) cards in my (\w+)')
def have_n_cards_in_my_y(self, num_cards, pile):
    setattr(world.deck, pile, [Dingus('fake card %d' % i) for i in range(int(num_cards))])

@step('I draw (\d+) cards')
def draw_n_cards(self, num):
    world.deck.draw_cards(num=int(num))


# Checks

@step('Playing a (\w+) should (\w+) raise an error')
def action_may_raise_error(self, card_type, yes_or_no):
    """This is imperfect, but for now we will always make sure this doesn't throw a CardNotInHandError."""
    card = Dingus('action_to_play',
            is_action=True,
            plus_actions = 0,
            plus_buys = 0,
            plus_cards = 0,
            plus_treasure = 0,
            )
    if card_type == 'action':
        card.is_action = True
    elif card_type == 'nonaction':
        card.is_action = False

    #TODO: Wow do not do this. Should really just determine how to add stubbed card we can use here by name.
    world.deck.hand.append(card)

    if yes_or_no == 'definitely':
        assert_raises(ActionError, world.deck.play_action, card)
    elif yes_or_no == 'not':
        # No check here will fail if this raised an exception
        world.deck.play_action(card)

@step('I check there is (\w+) VP in the deck')
def check_vp(self, num_vp):
    assert world.deck.count_vp() == int(num_vp)

@step('I check there is (\w+) treasure in the hand')
def check_treasure(self, num_treasure):
    assert world.deck.count_treasure() == int(num_treasure)

@step('I check the size of my (\w+) is (\d+)')
def check_size(self, pile, size):
    assert len(getattr(world.deck, pile)) == int(size)

@step('I check if I can buy a card worth (\d+)')
def can_buy_card(self, cost):
    card = Dingus('fake card', cost=int(cost))
    world.response = world.deck.can_buy(card)

@step("I am told (\w+)")
def check_response(self, resp):
    if resp == 'True':
        assert world.response
    else:
        assert not world.response

@step('Check that I have (\d+) cards in my (\w+)')
def have_n_cards_in_my_y(self, num_cards, pile):
    assert len(getattr(world.deck, pile)) == int(num_cards)


Feature: Drawing cards into the hand
    As a player with a deck
    I want to draw more cards into my hand

    Scenario Outline: Draw n cards
        Given I have a dummy deck
        And I have <num_hand> cards in my hand
        And I have <num_draw> cards in my draw
        And I have <num_discard> cards in my discard
        When I draw <num_to_draw> cards
        Then Check that I have <len_hand> cards in my hand
        And Check that I have <len_draw> cards in my draw
        And Check that I have <len_discard> cards in my discard

    Examples:
      | num_hand | num_draw | num_discard | num_to_draw | len_hand | len_draw | len_discard |
      | 0        | 1        | 0           | 1           | 1        | 0        | 0           |
      | 1        | 1        | 1           | 1           | 2        | 0        | 1           |
      | 0        | 1        | 3           | 2           | 2        | 2        | 0           |
      | 1        | 1        | 2           | 2           | 3        | 1        | 0           |

Feature: Initialize a deck
    I want a brand new deck to start with a shuffled draw pile and a full hand

    Scenario: Initialize a deck
        Given I have a new deck
        When I check the size of my hand
        Then I am told 5
        When I check the size of my discard
        Then I am told 0
        When I check the size of my draw
        Then I am told 5

    Examples:
      | buys | treasure | cost | response |
      | 1    | 5        | 5    | True     |
      | 0    | 5        | 5    | False    |
      | 1    | 4        | 5    | False    |
      | 0    | 4        | 5    | False    |

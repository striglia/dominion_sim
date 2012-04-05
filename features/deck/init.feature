Feature: Initialize a deck
    I want a brand new deck to start with a shuffled draw pile and a full hand

    Scenario: Initialize a deck
        Given I have a new deck
        Then I check the size of my hand is 5
        And I check the size of my discard is 0
        And I check the size of my draw is 5

Feature: Buy a card
    As a player with a deck
    I want to buy a card from the bank

    Scenario Outline: Buy a Market card
        Given I have a dummy deck
        And I have <buys> buys
        And I have <treasure> treasure
        When I check if I can buy a card worth <cost>
        Then I am told <response>

    Examples:
      | buys | treasure | cost | response |
      | 1    | 5        | 5    | True     |
      | 0    | 5        | 5    | False    |
      | 1    | 4        | 5    | False    |
      | 0    | 4        | 5    | False    |

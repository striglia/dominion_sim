Feature: Count VP in deck
    As a player with a deck
    I want to know how many VP are in my deck

    Scenario Outline: Count VP in a known deck
        Given I have a dummy deck
        And My <pile> has <card_num> cards with <vp_num> VP
        Then I check there is <total_vp> VP in the deck

    Examples:
      | pile | card_num | vp_num | total_vp |
      | hand | 1        | 1      | 1        |
      | hand | 2        | 2      | 4        |
      | draw | 1        | 1      | 1        |
      | draw | 2        | 2      | 4        |
      | discard | 1        | 1      | 1        |
      | discard | 2        | 2      | 4        |

    Scenario Outline: Count treasure in a known hand
        Given I have a dummy deck
        And My hand has <card_num> cards with <treasure_num> treasure
        Then I check there is <total_treasure> treasure in the hand

    Examples:
      | card_num | treasure_num | total_treasure |
      | 1        | 1            | 1              |
      | 2        | 2            | 4              |

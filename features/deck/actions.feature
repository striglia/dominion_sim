Feature: Only action cards can be played as actions
    As a player with a deck
    Action cards should be playable when money and actions permit

    Scenario Outline: Try to play a non-action with 
        Given I have a dummy deck
        And I have <num_actions> actions
        Then Playing a <card_type> should <yes_or_no> raise an error

    Examples:
      | num_actions | card_type | yes_or_no  |
      | 0           | nonaction | definitely |
      | 1           | nonaction | definitely |
      | 0           | action    | definitely |
      | 1           | action    | not        |

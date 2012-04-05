Feature: Cards should be well-defined
    For each defined card
    Values of various attributes should be well defined

    Scenario Outline: Validate a card's cost/vp/etc.
        Given I am considering the <card_name> card
        Then Validate the card's values

    Examples:
      | card_name |
      | Province |
      | Duchy |
      | Estate |
      | Curse |
      | Gold |
      | Silver |
      | Copper |
      | Village |
      | Smithy |
      | Laboratory |
      | Market |
      | Woodcutter |

Feature: Help

  Scenario: Basic help
    When I type "dotties help"
    Then I see the "help" screen

  Scenario: Specific help
    When I type "dotties help install"
    Then I see the "install help" screen

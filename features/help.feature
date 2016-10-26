Feature: Help

  Scenario: Basic help
    When I type "dotties help"
    Then I should see the "help" screen

  Scenario: Specific help
    When I type "dotties help install"
    Then I should see the "install help" screen

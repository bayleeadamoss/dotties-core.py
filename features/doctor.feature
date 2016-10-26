Feature: Doctor

  Scenario: I want to see if I have any conflicts
    Given I have "blainesch/dotties" installed
    And “~/.zshrc” is no longer owned by my user
    When I type "dotties doctor"
    Then I should see the "take ownership" screen

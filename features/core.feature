Feature: Core

  Scenario: Dotties without any arguments
    When I type "dotties"
    Then I should see the "help" screen

  Scenario: Sudo dotties should not do anything
    When I type "sudo dotties"
    Then I should see the "sudo of shame" screen

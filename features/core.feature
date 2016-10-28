Feature: Core

  Scenario: Dotties without any arguments
    When I type "dotties"
    Then I see the "help" screen

  Scenario: Sudo dotties fails for everything
    When I type "sudo dotties"
    Then I see the "sudo of shame" screen

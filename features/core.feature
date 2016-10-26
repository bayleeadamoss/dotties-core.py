Feature: Core

  Scenario: Factorial of 0
    When I type "dotties"
    Then I should see the "help" screen

  Scenario: Factorial of 0
    When I type "sudo dotties"
    Then I should see the "sudo of shame" screen

Feature: Version

  Scenario: I want to see my version
    When I type "dotties version"
    Then I should see the "version" screen

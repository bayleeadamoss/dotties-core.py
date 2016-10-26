Feature: Implode

  Scenario: I want to remove all of dotties
    Given I have "blainesch/dotties" installed
    When I type "dotties implode"
    Then I should have no dotties in "~/"
    And I have no dotties directory in "~/"

Feature: Uninstall

  Scenario: Uninstall my only package
    Given I have "blainesch/dotties" installed
    When I type "dotties uninstall blainesch/dotties"
    Then I have no dotties in "~/"

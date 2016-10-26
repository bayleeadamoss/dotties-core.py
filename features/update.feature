Feature: Update

  Scenario: Update re-clone deleted repos
    Given I have "blainesch/dotties" installed
    When I remove "blainesch/dotties" from the file system
    And I type "dotties update"
    Then I should see my dotfiles installed

  Scenario: Update re-creates deleted dotfiles
    Given I have "blainesch/dotties" installed
    When I remove all the dotties in "~/"
    And I type "dotties update"
    Then I should see my dotfiles installed

  Scenario: Update pulls the latest changes of all dotties
    Given an old version of "blainesch/dotties" installed
    And an old version of "amjith/dotties" installed
    When I type "dotties update"
    Then I should see the new version of "blainesch/dotties"
    And I should see the new version of "amjith/dotties"

  Scenario: Updating a specific dotfile doesn't upate all dotties
    Given an old version of "blainesch/dotties" installed
    And an old version of "amjith/dotties" installed
    When I type "dotties update blainesch/dotties"
    Then I should see the new version of "blainesch/dotties"
    And I should see the old version of "amjith/dotties"

  Scenario: Dry update
    Given I have an old version of "blainesch/dotties" installed
    When I type "dotties update --dry blainesch/dotties"
    Then I should see a list of files that would be installed

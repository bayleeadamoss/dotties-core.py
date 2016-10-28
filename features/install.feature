Feature: Install

  Scenario: Simple install
    Given I have no files in "~/"
    When I type "dotties install blainesch/dotties"
    Then I see my dotfiles installed

  Scenario: Install with file that already exists
    Given I have a file "~/.zshrc"
    When I type "dotties install blainesch/dotties"
    Then I am prompted asking if I want to overwrite "~/.zshrc"

  Scenario: Install with a file that already exists that I don't own
    Given I have a file "~/.zshrc" owned by root
    When I type "dotties install blainesch/dotties"
    And I choose "y" to overwrite "~/.zshrc"
    Then I see "Permission denied"
    And I am prompted asking if I want to overwrite "~/.zshrc"

  Scenario: Install with symlink that already exists
    Given I have a symlink "~/.zshrc"
    When I type "dotties install blainesch/dotties"
    Then I am prompted asking if I want to overwrite "~/.zshrc"

  Scenario: Install with a symlink that dotties owns already exists
    Given I have a dotties symlink "~/.zshrc"
    When I type "dotties install blainesch/dotties"
    Then I see my dotfiles installed

  Scenario: Install two root level packages
    Given I have no files in "~/"
    When I type "dotties install blainesch/dotties"
    And I type "dotties install amjith/dotties"
    Then I see both packages installed

  Scenario: Dry install
    When I type "dotties install --dry blainesch/dotties"
    Then I see a list of files that would be installed

  Scenario: Install a package that does not exist
    Given I have no files in "~/"
    When I type "dotties install tinytacoteam/does_-not_exist"
    Then I see the "repo of shame" screen

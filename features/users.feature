Feature: List known users

  Scenario: User list is visible in home page
    Given I visit the home page
    Then I see the user list

  Scenario: User list is sorted
    Given I visit the home page
    Then I see the first user is "Alice"
    Then I see the second user is "Bob"
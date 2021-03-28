Feature: Welcome visitors

  Scenario: Say hello from home page
    Given I visit the home page
    Then I see "hello world"
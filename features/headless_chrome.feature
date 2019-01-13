Feature: Headless Chrome runs successfully

  Scenario: I can use Headless Chrome in my BDD tests
    When I run the tests
    Then Headless chrome works normally

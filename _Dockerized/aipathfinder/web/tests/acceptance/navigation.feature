Feature: Test navigation between pages



  Scenario: Home can go to Login
    Given I am on the homepage
    When I click on the dropdown menu
    Given I wait for the dropdown to load
    When I click on the "Log In" dropdown link
    Then I am on the login page

  Scenario: Home can go to Logout
    Given I am on the homepage
    When I click on the dropdown menu
    Given I wait for the dropdown to load
    When I click on the "Log Out" dropdown link
    Then I am on the login page

  Scenario: Home can go to Register
    Given I am on the homepage
    When I click on the dropdown menu
    Given I wait for the dropdown to load
    When I click on the "Sign In" dropdown link
    Then I am on the register page


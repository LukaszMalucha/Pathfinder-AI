Feature: Test that page have correct content

  Scenario: Homepage has a correct title
    Given I am on the homepage
    Then There is a title shown on the page
    And The title tag has content "Pathfinder AI"

  Scenario: Signup page loads the form
   Given I am on the register page
   Then I can see there is a register form on the page

  Scenario: Login page loads the form
   Given I am on the login page
   Then I can see there is a login form on the page





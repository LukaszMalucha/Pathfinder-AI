Feature: Test that forms work correctly


  Scenario: Signup page registers user
    Given I am on the register page
    When I enter "tester" in the "username" field
    And I enter "tester@gmail.com" in the "email" field
    And I enter "12341234" in the "password" field
    And I press the submit button
    Then I am on the login page
#

  Scenario: Login page login user
    Given I am on the login page
    When I enter "tester" in the "username" login field
    And I enter "12341234" in the "password" login field
    And I press the login button
    Then I am on the homepage


  Scenario: Pathfinder AI works correctly
      Given I am on the homepage
      When I enter "1" in the "start_location" environment field
      When I enter "25" in the "astronauts" environment field
      When I enter "49" in the "base_location" environment field
      When I enter "33" in the "desert_storm_1" environment field
      When I enter "37" in the "desert_storm_2" environment field
      When I enter "41" in the "desert_storm_3" environment field
      When I enter "63" in the "desert_storm_4" environment field
      And I press the "BUILD THE ENVIRONMENT" button
      Given I wait for the algorithm page to load
      Then I am on the environment page
      Then I can see there are all key tiles displayed
      When I initiate pathfinder AI
      Given I wait for the algorithm page to load
      Then I am on the route page
      And I can see there is a path visible
      When I press the "Change Environment" button
      Then I am on the homepage






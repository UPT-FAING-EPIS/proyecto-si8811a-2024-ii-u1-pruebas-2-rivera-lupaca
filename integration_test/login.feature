Feature: Login Screen

Scenario: Check the presence and functionality of the login button
  Given I am on the login screen
  Then I expect the "Login with Microsoft" button to be present
  When I tap the "Login with Microsoft" button
  Then I expect to see a confirmation message "Login with Microsoft presionado"

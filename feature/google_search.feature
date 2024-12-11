Feature: Google Search

    @googleSearch
    Scenario: Search for a query on Google
        Then I go to "Inriver" url
        Then I wait for 5 Seconds
        Then I type "abfsk@clasohlson.se" in "Inriver_Email" textfield
        Then I click on "Inriver_Sign-in_Button"
        Then I wait for 10 Seconds
        Then I go to "Google" url
        Then I wait for 10 Seconds
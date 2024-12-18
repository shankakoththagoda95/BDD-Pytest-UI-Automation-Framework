Feature: All the sentences

Scenario: Common Sentences
    Then I wait for {seconds} Seconds
    Then I check the "{element}" element is Displayed
    Then I check the "{element}" element is Enabled
    Then I check the "{element}" element is Selected

Scenario: Windows related Sentences
    Then I check the Page title is "{title}"
    Then I "{window_Status}" the window
    Then I switch to {tab_number} tab
    Then I switch to "{frame}" frame
    Then I switch to frame number {index}
    Then I switch to default frame
    Then I check the dementions for the window
    Then I want to set the windows size to {width} x {height}
    Then I take a screenshot of the window
    Then I take a screenshot of the {element}
    Then I delete all cookies

Scenario: URL related Sentences
    Then I go to "{URL}" url
    Then I go back to the Page
    Then I go forward to the Page
    Then I refresh the page
    Then I check the ULR of "{URL}" is "{URL_text}"

Scenario: Mouse related Scentences
    Then I click on "{element}"
    Then I right-click on "{element}"
    Then I double-click on "{element}"

Scenario: Textfields related Sentences
    Then I clear the text in the "{element}" textfield
    Then I type "{text}" in "{element}" textfield
    Then I type "{text}" in "{element}" textfield and press Enter

Scenario: Label related Sentences
    Then I check the text in the "{element}" is "{text}"

Scenario: Dropdown related sentences
    Then I select "{option}" from the "{element}" dropdown

Scenario: CSS Related verifications
    Then I check the CSS value "{CSS_property}" of the "{element}"  is "{value}"
    Then I check the attribute "{attribute}" of the "{element}"  is "{value}"
    
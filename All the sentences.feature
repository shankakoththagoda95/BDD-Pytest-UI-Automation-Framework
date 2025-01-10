Feature: All the sentences

Scenario: Desktop Application related sentence
    Then I open the {app_name} application
    Then I close the {app_name} application
    Then I maximize the {app_name} window
    Then I minimize the {app_name} window
    Then I click the "{button_name}" button on {app_name}
    Then I enter "{text}" in the {control_name} text box on {app_name}
    Then I save the file as "{file_name}" in {encoding} encoding on {app_name}
    Then I open the file "{file_name}" in {app_name}

Scenario: Common Sentences
    Then I wait for {seconds} Seconds
    Then I verify that "{element}" is visible
    Then I verify that "{element}" is not visible
    Then I check the "{element}" element is Enabled
    Then I check the "{element}" element is Disabled
    Then I check the "{element}" element is Selected
    Then I check the tag og the "{element}" is "{tag_name}"

Scenario: Web Windows related Sentences
    Then I check the Page title is "{title}"
    Then I "{Maximize/Minimize/Fullscreen}" the window
    Then I check there are no other windows opens
    Then I switch to {tab_number} tab
    Then I switch to "{frame}" frame
    Then I switch to frame number {index}
    Then I switch to default frame
    Then I check the dementions for the window
    Then I want to set the windows size to {width} x {height}
    Then I take a screenshot of the window
    Then I take a screenshot of the {element}
    Then I delete all cookies
    Then I scroll to the "Top/Bottom" of the page
    

Scenario: URL related Sentences
    Then I go to "{URL}" url
    Then I go back to the Page
    Then I go forward to the Page
    Then I refresh the page
    Then I check the ULR of "{URL}" is "{URL_text}"


Scenario: Keyboard related Sentences
    Then I press the "{key}" in the Keyboard
    Then I type "{text}" while holding the "{key}" key


Scenario: Mouse related Scentences
    Then I click on "{element}"
    Then I right-click on "{element}"
    Then I double-click on "{element}"
    Then I hover over "{element}"
    Then I drag and Drop from "{}" to "{}"

Scenario: Textfields related Sentences
    Then I clear the text in the "{element}" textfield
    Then I type "{text}" in "{element}" textfield
    Then I type "{text}" in "{element}" textfield and press Enter

Scenario: Checkbox related Sentences
    Then I check the checkbox "{element}"
    Then I uncheck the checkbox "{element}"
    Then I verify the "{element}" checkbox is checked
    Then I verify the "{element}" checkbox is unchecked

Scenario: Label related Sentences
    Then I check the text in the "{element}" is "{text}"

Scenario: Dropdown related sentences
    Then I select "{option}" from the "{element}" dropdown
    Then I verify that the dropdown "{element}" has "{count}" options
    Then I verify that the dropdown "{element}" has "{option}" option

Scenario: CSS Related verifications
    Then I check the CSS value "{CSS_property}" of the "{element}"  is "{value}"
    Then I check the attribute "{attribute}" of the "{element}"  is "{value}"

Scenario: Upload files Related sentences
    Then I upload the "{file_name}" to "{Upload_locator}"
    
import os
import json
import pytest
import time
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

# Dynamically determine base directory
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Load Selectors and URLs
selectors_path = os.path.join(base_dir, 'web_selectors', 'google_selectors.json')
urls_path = os.path.join(base_dir, 'urls', 'urls.json')
with open(selectors_path) as f:
    selectors = json.load(f)
with open(urls_path) as f:
    urls = json.load(f)


# Fixture to initialize and close the browser
@pytest.fixture(scope="module")
def browser():
    # Path to msedgedriver.exe
    # Path to msedgedriver.exe
    edge_service = Service("msedgedriver.exe")
    
    # Suppress logs with options
    edge_options = Options()
    edge_options.add_argument("--log-level=3")  # Suppress all logs (ERROR level)
    
    # Initialize Edge WebDriver
    driver = webdriver.Edge(service=edge_service, options=edge_options)
    yield driver
    driver.quit()

# Load scenarios
scenarios(os.path.join(base_dir, 'feature', 'google_search.feature'))


# Step Definitions
# Windows related Sentences         -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@given(parsers.parse('I check the Page title is "{title}"'))
@when(parsers.parse('I check the Page title is "{title}"'))
@then(parsers.parse('I check the Page title is "{title}"'))
def go_forward(browser, title):
    try:
        page_title = browser.title
        assert page_title == title
        print(f"\033[94mThe page Title matched.\033[37m")
    except Exception as e:
        print(f"\033[91mFailed to match the Title. {page_title} => {title} Error: {str(e)}\033[37m")


@given(parsers.parse('I "{window_Status}" the window'))
@when(parsers.parse('I "{window_Status}" the window'))
@then(parsers.parse('I "{window_Status}" the window'))
def set_windows(browser, window_Status):
    try:
        if window_Status == "Maximize":
            browser.maximize_window()
        elif window_Status == "Minimize":
            browser.minimize_window()
        elif window_Status == "Fullscreen":
            browser.fullscreen_window()
    except KeyError:
        print(f"\033[91mWindow '{window_Status}'ed\033[37m")
    except Exception as e:
        print(f"\033[91mFailed to {window_Status}. Error: {str(e)}\033[37m")


@given(parsers.parse('I switch to {tab_number} tab'))
@when(parsers.parse('I switch to {tab_number} tab'))
@then(parsers.parse('I switch to {tab_number} tab'))
def switch_tabs(browser, tab_number):
    try:
        browser.switch_to_tab(int(tab_number))
    except KeyError:
        print(f"\033[91mSwitch to '{tab_number}'ed\033[37m")
    except Exception as e:
        print(f"\033[91mFailed to switch to {tab_number}. Error: {str(e)}\033[37m")


@given(parsers.parse('I check there are no other windows opens'))
@when(parsers.parse('I check there are no other windows opens'))
@then(parsers.parse('I check there are no other windows opens'))
def check_no_other_windows_open(browser):
    try:
        assert len(browser.window_handles) == 1
    except KeyError:
        print(f"\033[91mThere are no other windows opend\033[37m")
    except Exception as e:
        print(f"\033[91mOther windows checked failed. Error: {str(e)}\033[37m")


@given(parsers.parse('I switch to "{frame}" frame'))
@when(parsers.parse('I switch to "{frame}" frame'))
@then(parsers.parse('I switch to "{frame}" frame'))
def switch_frame(browser, frame):
    try:
        frame_element = browser.browser.find_element(By.CSS_SELECTOR, selectors[frame])
        browser.switch_to.frame(frame_element)
    except KeyError:
        print(f"\033[91mSwitched to '{frame}' frame\033[37m")
    except Exception as e:
        print(f"\033[91mFailed to switch to {frame}. Error: {str(e)}\033[37m")


@given(parsers.parse('I switch to frame number {index}'))
@when(parsers.parse('I switch to frame number {index}'))
@then(parsers.parse('I switch to frame number {index}'))
def switch_frame(browser, index):
    try:
        browser.switchTo().frame(int(index-1));
        print(f"\033[91mSwitched to frame number {index}\033[37m")
    except Exception as e:
        print(f"\033[91mFailed to switch to frame number {index}. Error: {str(e)}\033[37m")


@given(parsers.parse('I switch to default frame'))
@when(parsers.parse('I switch to default frame'))
@then(parsers.parse('I switch to default frame'))
def switch_default_frame(browser, frame):
    try:
        browser.switch_to.default_content()
        print(f"\033[91mSwitched to default frame\033[37m")
    except Exception as e:
        print(f"\033[91mFailed to switch to default frame. Error: {str(e)}\033[37m")


@given(parsers.parse('I check the dementions for the window'))
@when(parsers.parse('I check the dementions for the window'))
@then(parsers.parse('I check the dementions for the window'))
def window_dementions_ckeck(browser):
    try:
        width = browser.get_window_size().get("width")
        height = browser.get_window_size().get("height")
        print(f"\033[91mCurrent window dementions, Width:{width} Height:{height}\033[37m")
    except Exception as e:
        print(f"\033[91mFailed to switch to default frame. Error: {str(e)}\033[37m")


@given(parsers.parse('I want to set the windows size to {width} x {height}'))
@when(parsers.parse('I want to set the windows size to {width} x {height}'))
@then(parsers.parse('I want to set the windows size to {width} x {height}'))
def window_dementions_set(browser, width, height):
    try:
        width = int(width)
        height = int(height)
        browser.set_window_size(width, height)
        print(f"\033[91mCurrent window resized, Width:{width} Height:{height}\033[37m")
    except Exception as e:
        print(f"\033[91mFailed to switch to default frame. Error: {str(e)}\033[37m")


@given(parsers.parse('I take a screenshot of the window'))
@when(parsers.parse('I take a screenshot of the window'))
@then(parsers.parse('I take a screenshot of the window'))
def capture_screenshot(browser):
    try:
        browser.save_screenshot('./image.png')
    except KeyError:
        print(f"\033[91mScreenshot Captured\033[37m")
    except Exception as e:
        print(f"\033[91mFailed to capture screenshot. Error: {str(e)}\033[37m")


@given(parsers.parse('I take a screenshot of the {element}'))
@when(parsers.parse('I take a screenshot of the {element}'))
@then(parsers.parse('I take a screenshot of the {element}'))
def capture_screenshot_element(browser,element):
    try:
        ele = browser.find_element(By.CSS_SELECTOR, selectors[element])
        ele.screenshot('./image.png')
    except KeyError:
        print(f"\033[91m{element} screenshot Captured\033[37m")
    except Exception as e:
        print(f"\033[91mFailed to capture {element} screenshot. Error: {str(e)}\033[37m")



@given(parsers.parse('I delete all cookies'))
@when(parsers.parse('I delete all cookies'))
@then(parsers.parse('I delete all cookies'))
def delete_cookiees(browser):
    try:
        browser.delete_all_cookies()
    except KeyError:
        print(f"\033[91mAll the cookies are deletet\033[37m")
    except Exception as e:
        print(f"\033[91mFailed to delete cookies. Error: {str(e)}\033[37m")


# URL Related Sentences         -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@given(parsers.parse('I go to "{URL}" url'))
@when(parsers.parse('I go to "{URL}" url'))
@then(parsers.parse('I go to "{URL}" url'))
def go_to_google(browser, URL):
    try:
        google_url = urls[URL]
        browser.get(google_url)
        print(f"Opened the {URL} URL.")
    except KeyError:
        print(f"\033[91mURL '{URL}' not found in the configuration.\033[37m")
    except Exception as e:
        print(f"\033[91mFailed to open {URL}. Error: {str(e)}\033[37m")


@given(parsers.parse('I go back to the Page'))
@when(parsers.parse('I go back to the Page'))
@then(parsers.parse('I go back to the Page'))
def go_back(browser):
    try:
        browser.back()
        print(f"\033[94mWent to the Previously visited page.\033[37m")
    except Exception as e:
        print(f"\033[91mFailed to go back to the page. Error: {str(e)}\033[37m")


@given(parsers.parse('I go forward to the Page'))
@when(parsers.parse('I go forward to the Page'))
@then(parsers.parse('I go forward to the Page'))
def go_forward(browser):
    try:
        browser.forward()
        print(f"\033[94mWent Forward to the page.\033[37m")
    except Exception as e:
        print(f"\033[91mFailed to go forward to the page. Error: {str(e)}\033[37m")


@given(parsers.parse('I refresh the page'))
@when(parsers.parse('I refresh the page'))
@then(parsers.parse('I refresh the page'))
def go_to_url(browser):
    try:
        browser.refresh()
        print(f"\033[94mPage Refreshed.\033[37m")
    except Exception as e:
        print(f"\033[91mFailed to refresh the page. Error: {str(e)}\033[37m")


@given(parsers.parse('I check the ULR of "{URL}" is "{URL_text}"'))
@when(parsers.parse('I check the ULR of "{URL}" is "{URL_text}"'))
@then(parsers.parse('I check the ULR of "{URL}" is "{URL_text}"'))
def check_current_url(browser, URL, URL_text):
    try:
        web_url = urls[URL]
        browser.get(web_url)
        current_url = browser.current_url
        assert current_url == URL_text, f"\033[31mExpected URL '{URL_text}', but found '{current_url}'\033[37m"
        print("\033[94mURL checked with Given URL.\033[37m")
    except KeyError:
        print(f"\033[31mURL '{URL}' not found in the URL dictionary.\033[37m")
        assert False, f"URL '{URL}' is missing in the provided URL dictionary."
    except WebDriverException as e:
        print(f"\033[31mWebDriverException encountered: {str(e)}\033[37m")
        assert False, f"Failed to navigate to URL '{web_url}'. Error: {str(e)}"
    except AssertionError as ae:
        print(str(ae))
        assert False, str(ae)    


@given(parsers.parse('I wait for {seconds} Seconds'))
@when(parsers.parse('I wait for {seconds} Seconds'))
@then(parsers.parse('I wait for {seconds} Seconds'))
def wait_seconds(seconds):
    time.sleep(int(seconds))  # Wait for 5 seconds
    print(f"waited for{seconds} seconds")


# Common element Related Sentences         -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@given(parsers.parse('I verify that "{element}" is visible'))
@when(parsers.parse('I verify that "{element}" is visible'))
@then(parsers.parse('I verify that "{element}" is visible'))
def check_is_dispalyed(browser, element):    
    try:
        is_email_visible = browser.find_element(By.CSS_SELECTOR, selectors[element]).is_displayed()
        assert is_email_visible == True
        print(f"\033[94m'{element} checked with Displayed.\033[37m")
    except NoSuchElementException:
        print(f"\033[31mNo such element '{element}' was found on the page.\033[37m")
        assert False, f"Element '{element}' not found."
    except TimeoutException:
        print("\033[31mTimeout while trying to find the element.\033[37m")
        assert False, f"Timeout while waiting for the element '{element}'."
    except WebDriverException as e:
        print(f"\033[31mWebDriverException encountered: {str(e)}\033[37m")
        assert False, f"WebDriverException: {str(e)}"


@given(parsers.parse('I verify that "{element}" is not visible'))
@when(parsers.parse('I verify that "{element}" is not visible'))
@then(parsers.parse('I verify that "{element}" is not visible'))
def check_isnot__dispalyed(browser, element):    
    try:
        is_email_visible = browser.find_element(By.CSS_SELECTOR, selectors[element]).is_displayed()
        assert is_email_visible == False
        print(f"\033[94m'{element} checked with not Displayed.\033[37m")
    except NoSuchElementException:
        print(f"\033[31mNo such element '{element}' was found on the page.\033[37m")
        assert False, f"Element '{element}' not found."
    except TimeoutException:
        print("\033[31mTimeout while trying to find the element.\033[37m")
        assert False, f"Timeout while waiting for the element '{element}'."
    except WebDriverException as e:
        print(f"\033[31mWebDriverException encountered: {str(e)}\033[37m")
        assert False, f"WebDriverException: {str(e)}"


@given(parsers.parse('I check the "{element}" element is Enabled'))
@when(parsers.parse('I check the "{element}" element is Enabled'))
@then(parsers.parse('I check the "{element}" element is Enabled'))
def check_is_enabled(browser, element):       
    try:
        is_enabled_button = browser.find_element(By.CSS_SELECTOR, selectors[element]).is_enabled()
        assert is_enabled_button == True
        print(f"\033[94m'{element} checked with Enabled.\033[37m")
    except NoSuchElementException:
        print(f"\033[31mNo such element '{element}' was found on the page.\033[37m")
        assert False, f"Element '{element}' not found."
    except TimeoutException:
        print("\033[31mTimeout while trying to find the element.\033[37m")
        assert False, f"Timeout while waiting for the element '{element}'."
    except WebDriverException as e:
        print(f"\033[31mWebDriverException encountered: {str(e)}\033[37m")
        assert False, f"WebDriverException: {str(e)}"


@given(parsers.parse('I check the "{element}" element is Disabled'))
@when(parsers.parse('I check the "{element}" element is Disabled'))
@then(parsers.parse('I check the "{element}" element is Disabled'))
def check_is_disabled(browser, element):       
    try:
        is_enabled_button = browser.find_element(By.CSS_SELECTOR, selectors[element]).is_enabled()
        assert is_enabled_button == False
        print(f"\033[94m'{element} checked with Disabled.\033[37m")
    except NoSuchElementException:
        print(f"\033[31mNo such element '{element}' was found on the page.\033[37m")
        assert False, f"Element '{element}' not found."
    except TimeoutException:
        print("\033[31mTimeout while trying to find the element.\033[37m")
        assert False, f"Timeout while waiting for the element '{element}'."
    except WebDriverException as e:
        print(f"\033[31mWebDriverException encountered: {str(e)}\033[37m")
        assert False, f"WebDriverException: {str(e)}"


@given(parsers.parse('I check the "{element}" element is Selected'))
@when(parsers.parse('I check the "{element}" element is Selected'))
@then(parsers.parse('I check the "{element}" element is Selected'))
def check_is_selected(browser, element):   
    try:
        is_selected_check = browser.find_element(By.CSS_SELECTOR, selectors[element]).is_selected()
        assert is_selected_check == True
        print(f"\033[94m'{element} checked with Selected.\033[37m")
    except NoSuchElementException:
        print(f"\033[31mNo such element '{element}' was found on the page.\033[37m")
        assert False, f"Element '{element}' not found."
    except TimeoutException:
        print("\033[31mTimeout while trying to find the element.\033[37m")
        assert False, f"Timeout while waiting for the element '{element}'."
    except WebDriverException as e:
        print(f"\033[31mWebDriverException encountered: {str(e)}\033[37m")
        assert False, f"WebDriverException: {str(e)}"


@given(parsers.parse('I check the "{element}" element is not Selected'))
@when(parsers.parse('I check the "{element}" element is not Selected'))
@then(parsers.parse('I check the "{element}" element is not Selected'))
def check_is_not_selected(browser, element):   
    try:
        is_selected_check = browser.find_element(By.CSS_SELECTOR, selectors[element]).is_selected()
        assert is_selected_check == False
        print(f"\033[94m'{element} checked with not Selected.\033[37m")
    except NoSuchElementException:
        print(f"\033[31mNo such element '{element}' was found on the page.\033[37m")
        assert False, f"Element '{element}' not found."
    except TimeoutException:
        print("\033[31mTimeout while trying to find the element.\033[37m")
        assert False, f"Timeout while waiting for the element '{element}'."
    except WebDriverException as e:
        print(f"\033[31mWebDriverException encountered: {str(e)}\033[37m")
        assert False, f"WebDriverException: {str(e)}"


@given(parsers.parse('I check the tag og the "{element}" is "{tag_name}"'))
@when(parsers.parse('I check the tag og the "{element}" is "{tag_name}"'))
@then(parsers.parse('I check the tag og the "{element}" is "{tag_name}"'))
def go_to_url(browser, element, tag_name):
    try:
        tag_name_inp = browser.find_element(By.CSS_SELECTOR, selectors[element]).tag_name
        assert tag_name_inp == tag_name
        print(f"\033[94mTag name checked. Element:{element}, Tag:{tag_name}.\033[37m")
    except Exception as e:
        print(f"\033[91mFailed to refresh the page. Error: {str(e)}\033[37m")


# CSS verification related Sentences         -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@given(parsers.parse('I check the CSS value "{CSS_property}" of the "{element}"  is "{value}"'))
@when(parsers.parse('I check the CSS value "{CSS_property}" of the "{element}"  is "{value}"'))
@then(parsers.parse('I check the CSS value "{CSS_property}" of the "{element}"  is "{value}"'))
def check_CSS_properties(browser, element, CSS_property, value):   
    try:
        web_element = browser.find_element(By.CSS_SELECTOR, selectors[element])
        web_element_info = str(web_element.value_of_css_property(CSS_property))
        assert web_element_info == str(value)
        print(f"\033[94m'{element} has the {CSS_property} CSS as {value}.\033[37m")
    except NoSuchElementException:
        print(f"\033[31mNo such element '{element}' was found on the page.\033[37m")
        assert False, f"Element '{element}' not found."
    except TimeoutException:
        print("\033[31mTimeout while trying to find the element.\033[37m")
        assert False, f"Timeout while waiting for the element '{element}'."
    except WebDriverException as e:
        print(f"\033[31mWebDriverException encountered: {str(e)}\033[37m")
        assert False, f"WebDriverException: {str(e)}"


@given(parsers.parse('I check the attribute "{attribute}" of the "{element}"  is "{value}"'))
@when(parsers.parse('I check the attribute "{attribute}" of the "{element}"  is "{value}"'))
@then(parsers.parse('I check the attribute "{attribute}" of the "{element}"  is "{value}"'))
def check_Attribute_values(browser, element, attribute, value):   
    try:
        web_element = browser.find_element(By.CSS_SELECTOR, selectors[element])
        web_element_info = str(web_element.get_attribute(attribute))
        assert web_element_info == str(value)
        print(f"\033[94m'{element} has the {attribute} attribure as {value}.\033[37m")
    except NoSuchElementException:
        print(f"\033[31mNo such element '{element}' was found on the page.\033[37m")
        assert False, f"Element '{element}' not found."
    except TimeoutException:
        print("\033[31mTimeout while trying to find the element.\033[37m")
        assert False, f"Timeout while waiting for the element '{element}'."
    except WebDriverException as e:
        print(f"\033[31mWebDriverException encountered: {str(e)}\033[37m")
        assert False, f"WebDriverException: {str(e)}"


# Mouse Related Sentences         -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@given(parsers.parse('I click on "{element}"'))
@when(parsers.parse('I click on "{element}"'))
@then(parsers.parse('I click on "{element}"'))
def click_on_button(browser, element):
    try:
        button = browser.find_element(By.CSS_SELECTOR, selectors[element])
        button.click()
        time.sleep(1)
        print(f"\033[94m{element} clicked.\033[37m")
    except NoSuchElementException:
        print(f"\033[31mNo such element '{element}' was found on the page.\033[37m")
        assert False, f"Element '{element}' not found."
    except TimeoutException:
        print("\033[31mTimeout while trying to find the element.\033[37m")
        assert False, f"Timeout while waiting for the element '{element}'."
    except WebDriverException as e:
        print(f"\033[31mWebDriverException encountered: {str(e)}\033[37m")
        assert False, f"WebDriverException: {str(e)}"


@given(parsers.parse('I right-click on "{element}"'))
@when(parsers.parse('I right-click on "{element}"'))
@then(parsers.parse('I right-click on "{element}"'))
def right_click_on_element(browser, element):
    try:
        target_element = browser.find_element(By.CSS_SELECTOR, selectors[element])
        actions = ActionChains(browser)
        actions.context_click(target_element).perform()
        print(f"\033[94mRight-click performed on '{element}'.\033[37m")
    except NoSuchElementException:
        print(f"\033[31mNo such element '{element}' was found on the page.\033[37m")
        assert False, f"Element '{element}' not found."
    except TimeoutException:
        print("\033[31mTimeout while trying to find the element.\033[37m")
        assert False, f"Timeout while waiting for the element '{element}'."
    except WebDriverException as e:
        print(f"\033[31mWebDriverException encountered: {str(e)}\033[37m")
        assert False, f"WebDriverException: {str(e)}"


@given(parsers.parse('I double-click on "{element}"'))
@when(parsers.parse('I double-click on "{element}"'))
@then(parsers.parse('I double-click on "{element}"'))
def double_click_on_element(browser, element):
    try:
        target_element = browser.find_element(By.CSS_SELECTOR, selectors[element])
        actions = ActionChains(browser)
        actions.double_click(target_element).perform()
        print(f"\033[94mDouble-click performed on '{element}'.\033[37m")
    except NoSuchElementException:
        print(f"\033[31mNo such element '{element}' was found on the page.\033[37m")
        assert False, f"Element '{element}' not found."
    except TimeoutException:
        print("\033[31mTimeout while trying to find the element.\033[37m")
        assert False, f"Timeout while waiting for the element '{element}'."
    except WebDriverException as e:
        print(f"\033[31mWebDriverException encountered: {str(e)}\033[37m")
        assert False, f"WebDriverException: {str(e)}"


@given(parsers.parse('I hover over "{element}"'))
@when(parsers.parse('I hover over "{element}"'))
@then(parsers.parse('I hover over "{element}"'))
def hover_on_element(browser, element):
    try:
        target_element = browser.find_element(By.CSS_SELECTOR, selectors[element])
        actions = ActionChains(browser).move_to_element(target_element)
        actions.perform()
        print(f"\033[94mDouble-click performed on '{element}'.\033[37m")
    except NoSuchElementException:
        print(f"\033[31mNo such element '{element}' was found on the page.\033[37m")
        assert False, f"Element '{element}' not found."
    except TimeoutException:
        print("\033[31mTimeout while trying to find the element.\033[37m")
        assert False, f"Timeout while waiting for the element '{element}'."
    except WebDriverException as e:
        print(f"\033[31mWebDriverException encountered: {str(e)}\033[37m")
        assert False, f"WebDriverException: {str(e)}"


# Keyboard Related Sentences         -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@given(parsers.parse('I press the "{key}" in the Keyboard'))
@when(parsers.parse('I press the "{key}" in the Keyboard'))
@then(parsers.parse('I press the "{key}" in the Keyboard'))
def press_keyboard_keys(browser, key):
    try:
        ActionChains(browser)\
            .key_down(Keys.key)\
            .key_up(Keys.key)\
            .perform()
        print(f"\033[94mPress the {key} key in the Keyboard.\033[37m")
    except WebDriverException as e:
        print(f"\033[31mWebDriverException encountered: {str(e)}\033[37m")
        assert False, f"WebDriverException: {str(e)}"


@given(parsers.parse('I type "{text}" while holding the "{key}" key'))
@when(parsers.parse('I type "{text}" while holding the "{key}" key'))
@then(parsers.parse('I type "{text}" while holding the "{key}" key'))
def tyep_while_holding_keys(browser, text, key):
    try:
        ActionChains(browser)\
            .key_down(Keys.key)\
            .send_keys(text)\
            .key_up(Keys.key)\
            .perform()
        print(f"\033[94mtype {text} while holding the {key} key.\033[37m")
    except WebDriverException as e:
        print(f"\033[31mWebDriverException encountered: {str(e)}\033[37m")
        assert False, f"WebDriverException: {str(e)}"


# Textfield Related Sentences         -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@given(parsers.parse('I clear the text in the "{element}" textfield'))
@when(parsers.parse('I clear the text in the "{element}" textfield'))
@then(parsers.parse('I clear the text in the "{element}" textfield'))
def type_in_textfield(browser,element):
    try:
        textfield = browser.find_element(By.CSS_SELECTOR, selectors[element])
        textfield.clear()
        print(f"\033[94m{element} Cleared.\033[37m")
    except NoSuchElementException:
        print(f"\033[31mNo such element '{element}' was found on the page.\033[37m")
        assert False, f"Element '{element}' not found."
    except TimeoutException:
        print("\033[31mTimeout while trying to find the element.\033[37m")
        assert False, f"Timeout while waiting for the element '{element}'."
    except WebDriverException as e:
        print(f"\033[31mWebDriverException encountered: {str(e)}\033[37m")
        assert False, f"WebDriverException: {str(e)}"        


@given(parsers.parse('I type "{text}" in "{element}" textfield'))
@when(parsers.parse('I type "{text}" in "{element}" textfield'))
@then(parsers.parse('I type "{text}" in "{element}" textfield'))
def type_in_textfield(browser,text,element):
    try:
        textfield = browser.find_element(By.CSS_SELECTOR, selectors[element])
        textfield.send_keys(text)
        print(f"\033[94m{element} populated.\033[37m")
    except NoSuchElementException:
        print(f"\033[31mNo such element '{element}' was found on the page.\033[37m")
        assert False, f"Element '{element}' not found."
    except TimeoutException:
        print("\033[31mTimeout while trying to find the element.\033[37m")
        assert False, f"Timeout while waiting for the element '{element}'."
    except WebDriverException as e:
        print(f"\033[31mWebDriverException encountered: {str(e)}\033[37m")
        assert False, f"WebDriverException: {str(e)}"


@given(parsers.parse('I type "{text}" in "{element}" textfield and press Enter'))
@when(parsers.parse('I type "{text}" in "{element}" textfield and press Enter'))
@then(parsers.parse('I type "{text}" in "{element}" textfield and press Enter'))
def type_in_textfield_press_enter(browser,text,element):
    try:
        textfield = browser.find_element(By.CSS_SELECTOR, selectors[element])
        textfield.send_keys(text + Keys.ENTER)
        print(f"\033[94m{element} populated and pressed Enter.\033[37m")
    except NoSuchElementException:
        print(f"\033[31mNo such element '{element}' was found on the page.\033[37m")
        assert False, f"Element '{element}' not found."
    except TimeoutException:
        print("\033[31mTimeout while trying to find the element.\033[37m")
        assert False, f"Timeout while waiting for the element '{element}'."
    except WebDriverException as e:
        print(f"\033[31mWebDriverException encountered: {str(e)}\033[37m")
        assert False, f"WebDriverException: {str(e)}"


# Checkbox Related Sentences         -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@given(parsers.parse('I check the checkbox "{element}"'))
@when(parsers.parse('I check the checkbox "{element}"'))
@then(parsers.parse('I check the checkbox "{element}"'))
def uncheck_checkbox(browser, element):
    try:
        checkbox = browser.find_element(By.CSS_SELECTOR, selectors[element])
        if not checkbox.is_selected():
            checkbox.click()
            print(f"\033[94mCheckbox '{element}' has been checked.\033[37m")
        else:
            print(f"\033[93mCheckbox '{element}' was already checked.\033[37m")
    except NoSuchElementException:
        print(f"\033[31mNo such checkbox '{element}' was found on the page.\033[37m")
        assert False, f"Checkbox '{element}' not found."
    except TimeoutException:
        print("\033[31mTimeout while trying to find the checkbox.\033[37m")
        assert False, f"Timeout while waiting for the checkbox '{element}'."
    except WebDriverException as e:
        print(f"\033[31mWebDriverException encountered: {str(e)}\033[37m")
        assert False, f"WebDriverException: {str(e)}"


@given(parsers.parse('I uncheck the checkbox "{element}"'))
@when(parsers.parse('I uncheck the checkbox "{element}"'))
@then(parsers.parse('I uncheck the checkbox "{element}"'))
def uncheck_checkbox(browser, element):
    try:
        checkbox = browser.find_element(By.CSS_SELECTOR, selectors[element])
        if checkbox.is_selected():
            checkbox.click()
            print(f"\033[94mCheckbox '{element}' has been unchecked.\033[37m")
        else:
            print(f"\033[93mCheckbox '{element}' was already unchecked.\033[37m")
    except NoSuchElementException:
        print(f"\033[31mNo such checkbox '{element}' was found on the page.\033[37m")
        assert False, f"Checkbox '{element}' not found."
    except TimeoutException:
        print("\033[31mTimeout while trying to find the checkbox.\033[37m")
        assert False, f"Timeout while waiting for the checkbox '{element}'."
    except WebDriverException as e:
        print(f"\033[31mWebDriverException encountered: {str(e)}\033[37m")
        assert False, f"WebDriverException: {str(e)}"


@given(parsers.parse('Then I verify the "{element}" checkbox is checked'))
@when(parsers.parse('Then I verify the "{element}" checkbox is checked'))
@then(parsers.parse('Then I verify the "{element}" checkbox is checked'))
def uncheck_checkbox(browser, element):
    try:
        checkbox = browser.find_element(By.CSS_SELECTOR, selectors[element])
        assert checkbox.is_selected()
        print(f"\033[94mCheckbox '{element}' is checked.\033[37m")
    except NoSuchElementException:
        print(f"\033[31mNo such checkbox '{element}' was found on the page.\033[37m")
        assert False, f"Checkbox '{element}' not found."
    except TimeoutException:
        print("\033[31mTimeout while trying to find the checkbox.\033[37m")
        assert False, f"Timeout while waiting for the checkbox '{element}'."
    except WebDriverException as e:
        print(f"\033[31mWebDriverException encountered: {str(e)}\033[37m")
        assert False, f"WebDriverException: {str(e)}"


@given(parsers.parse('Then I verify the "{element}" checkbox is unchecked'))
@when(parsers.parse('Then I verify the "{element}" checkbox is unchecked'))
@then(parsers.parse('Then I verify the "{element}" checkbox is unchecked'))
def uncheck_checkbox(browser, element):
    try:
        checkbox = browser.find_element(By.CSS_SELECTOR, selectors[element])
        assert not checkbox.is_selected()
        print(f"\033[94mCheckbox '{element}' is unchecked.\033[37m")
    except NoSuchElementException:
        print(f"\033[31mNo such checkbox '{element}' was found on the page.\033[37m")
        assert False, f"Checkbox '{element}' not found."
    except TimeoutException:
        print("\033[31mTimeout while trying to find the checkbox.\033[37m")
        assert False, f"Timeout while waiting for the checkbox '{element}'."
    except WebDriverException as e:
        print(f"\033[31mWebDriverException encountered: {str(e)}\033[37m")
        assert False, f"WebDriverException: {str(e)}"


# Label Related Sentences         -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@given(parsers.parse('I check the text in the "{element}" is "{text}"'))
@when(parsers.parse('I check the text in the "{element}" is "{text}"'))
@then(parsers.parse('I check the text in the "{element}" is "{text}"'))
def check_the_text_label(browser, text, element):
    try:
        textfield = browser.find_element(By.CSS_SELECTOR, selectors[element])
        element_text = textfield.text
        print(f"\033[94mThe text in the element '{element}' is '{element_text}'.\033[37m")
        assert element_text == text, f"\033[31mExpected text '{text}', but found '{element_text}'\033[37m"
    except NoSuchElementException:
        print(f"\033[31mNo such element '{element}' was found on the page.\033[37m")
        assert False, f"Element '{element}' not found."
    except TimeoutException:
        print("\033[31mTimeout while trying to find the element.\033[37m")
        assert False, f"Timeout while waiting for the element '{element}'."
    except WebDriverException as e:
        print(f"\033[31mWebDriverException encountered: {str(e)}\033[37m")
        assert False, f"WebDriverException: {str(e)}"


# Dropdown Related Sentences         -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@given(parsers.parse('I select "{option}" from the "{element}" dropdown'))
@when(parsers.parse('I select "{option}" from the "{element}" dropdown'))
@then(parsers.parse('I select "{option}" from the "{element}" dropdown'))
def select_from_dropdown(browser, option, element):
    try:
        dropdown = browser.find_element(By.CSS_SELECTOR, selectors[element])
        select = Select(dropdown)
        select.select_by_visible_text(option)
        print(f"\033[94mOption '{option}' selected in the '{element}' dropdown.\033[37m")
    except NoSuchElementException:
        print(f"\033[31mNo such dropdown element '{element}' was found on the page.\033[37m")
        assert False, f"Dropdown element '{element}' not found."
    except TimeoutException:
        print("\033[31mTimeout while trying to find the dropdown element.\033[37m")
        assert False, f"Timeout while waiting for the dropdown element '{element}'."
    except WebDriverException as e:
        print(f"\033[31mWebDriverException encountered: {str(e)}\033[37m")
        assert False, f"WebDriverException: {str(e)}"


# File Upload related Sentences     -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@given(parsers.parse('I upload the "{file_name}" to "{locator}"'))
@when(parsers.parse('I upload the "{file_name}" to "{locator}"'))
@then(parsers.parse('I upload the "{file_name}" to "{locator}"'))
def select_from_dropdown(browser, file_name, locator):
    try:
        upload_file = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", file_name))
        file_input = browser.find_element(By.CSS_SELECTOR, selectors[locator])
        file_input.send_keys(upload_file)
    except NoSuchElementException:
        print(f"\033[31mNo such dropdown element '{locator}' was found on the page.\033[37m")
        assert False, f"Dropdown element '{locator}' not found."
    except TimeoutException:
        print("\033[31mTimeout while trying to find the dropdown element.\033[37m")
        assert False, f"Timeout while waiting for the dropdown element '{locator}'."
    except WebDriverException as e:
        print(f"\033[31mWebDriverException encountered: {str(e)}\033[37m")
        assert False, f"WebDriverException: {str(e)}"
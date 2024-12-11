import os
import json
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.edge.options import Options
from pytest_bdd import scenarios, given, when, then, parsers


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
@then(parsers.parse('I go to "{URL}" url'))
def go_to_google(browser, URL):
    google_url = urls[URL]
    browser.get(google_url)
    print("Opened Google URL.")

@then(parsers.parse('I wait for {seconds} Seconds'))
def wait_seconds(seconds):
    time.sleep(int(seconds))  # Wait for 5 seconds
    print(f"waited for{seconds} seconds")

@then(parsers.parse('I click on "{element}"'))
def click_on_search(browser, element):
    button = browser.find_element(By.CSS_SELECTOR, selectors[element])
    button.click()
    print(f"{element} clicked")

@then(parsers.parse('I type "{text}" in "{element}" textfield'))
def click_on_search(browser,text,element):
    textfield = browser.find_element(By.CSS_SELECTOR, selectors[element])
    textfield.send_keys(text)
    print(f"{element} populated")

@then(parsers.parse('I check the text in the "{element}" is"{text}"'))
def click_on_search(browser,text,element):
    textfield = browser.find_element(By.CSS_SELECTOR, selectors[element])
    element_text = textfield.get_text(text)
    print(f"{element_text} populated")

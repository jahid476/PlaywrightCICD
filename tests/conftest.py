import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def page():
    with sync_playwright() as playwright:
        #Lunch the chrome browser in non headless mode
        browser = playwright.chromium.launch(headless=False)
        #Create an isolated browser context(incognito mode)
        context = browser.new_context()
        #Create a new page in the browser context
        page=context.new_page()
        #Return the page object to the test unction
        yield page
        #After test is done, close browser context and browser
        context.close()
        browser.close()
import re
import time
#from playwright.sync_api import Playwright, expect
from playwright.sync_api import sync_playwright, expect

def test_multiple_window():
    """Handling multpile tabs and multiple window are same, no separate script for both of these"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://demo.automationtesting.in/Windows.html")
        
        page.get_by_role("link", name="Open Seperate Multiple Windows").click()
        page.wait_for_timeout(3000)
        page.get_by_role("button", name="click").click()
        page.wait_for_timeout(3000)
        #Get all pages opened
        all_pages =context.pages
        print("Total Number of Pages :", len(all_pages))
        page.wait_for_timeout(3000)
        for current_page in all_pages:
                if current_page.title()=="Index":
                    print("Title of the window:", current_page.title())
                    current_page.bring_to_front()
                    current_page.get_by_placeholder("Email id for Sign Up").fill("Sayed")
        page.wait_for_timeout(3000)
        page.bring_to_front()
        page.wait_for_timeout(3000)

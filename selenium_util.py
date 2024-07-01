import os
import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def search_title_name(browser):
    browser.maximize_window()
    browser.execute_script("window.scrollBy(0,500)", "")
    time.sleep(10)
    title_name = WebDriverWait(browser, 30).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, "//label[@for='accordion-item-titleNameAccordion']")))
    title_name.click()
    action = ActionChains(browser)
    a = WebDriverWait(browser, 20).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "(//div[@role='presentation'])[34]")))
    action.key_down(Keys.CONTROL).click(a).key_up(Keys.CONTROL).send_keys("CaptainMiller").perform()
    see_results = WebDriverWait(browser, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//button[@aria-label='See results']")))
    WebDriverWait(browser, 10)
    action.double_click(see_results).perform()
    WebDriverWait(browser, 10)
    print("Title name:search Done")
    print("URL:", browser.current_url)


def save_screenshot(browser):
    screenshot_dir = os.path.join(os.getcwd(), 'screenshot')
    os.makedirs(screenshot_dir, exist_ok=True)
    screenshot_path = os.path.join(screenshot_dir, f"search_success.png")
    browser.save_screenshot(screenshot_path)
    print(f"screenshot saved at: {screenshot_path}")

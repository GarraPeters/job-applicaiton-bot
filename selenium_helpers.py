import random
import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

AGENT = (
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/60.0.3112.50 Safari/537.36'
)


def get_chrome_options():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1920,10000')
    chrome_options.add_argument(f'--user-agent={AGENT}')
    return chrome_options


def find(browser, selector):
    wait_time = 3
    try:
        return WebDriverWait(browser, wait_time).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,
                                                               selector)))
    except TimeoutException as exc:
        raise LookupError(f'{selector} not found') from exc


def start_browser():
    browser = webdriver.Chrome(options=get_chrome_options())
    browser.maximize_window()
    browser.implicitly_wait(3)
    return browser


def send_keys(element, letters):
    for letter in letters:
        time.sleep(random.uniform(0.5, 1.5))
        element.send_keys(letter)

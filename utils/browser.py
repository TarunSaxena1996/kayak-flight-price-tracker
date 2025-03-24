# utils/browser.py
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options

def launch_browser(headless=False):
    options = uc.ChromeOptions()
    if headless:
        options.headless = True
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-extensions")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")

    driver = uc.Chrome(options=options)
    return driver
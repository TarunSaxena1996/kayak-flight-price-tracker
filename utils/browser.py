# utils/browser.py
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def launch_browser(headless=False):
    #options = uc.ChromeOptions() used for by passing bot detection
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless=new") 
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-extensions")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")

    # 🔹 Initialize WebDriver with ChromeOptions
    service = Service()  # You can specify the path to chromedriver if needed
    driver = webdriver.Chrome(service=service, options=options)
    return driver
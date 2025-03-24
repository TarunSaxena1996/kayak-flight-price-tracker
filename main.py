'''
from utils.browser import launch_browser
import time

def test_browser():
    driver = launch_browser(headless=False)
    driver.get("https://www.kayak.com/flights")
    time.sleep(10)
    driver.quit()

if __name__ == "__main__":
    test_browser()

'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Setup Chrome
options = Options()
options.add_argument("--start-maximized")
# options.add_argument("--headless")  # comment out if you want to see browser actions
service = Service()

driver = webdriver.Chrome(service=service, options=options)

# Open Kayak
driver.get("https://www.kayak.com/flights")

time.sleep(5)  # let the page load completely

# Example static search:
departure_city = "New York"
destination_city = "London"
departure_date = "2024-04-01"
return_date = "2024-04-10"

# You'll need to find the input boxes and enter these values. We'll do this next.

# For now, just print title and quit:
print(driver.title)

# Fill departure city
departure_input = driver.find_element(By.XPATH, "//input[@aria-label='Flight origin input']")
departure_input.click()
time.sleep(1)
departure_input.send_keys(Keys.CONTROL + "a")  # select all text
departure_input.send_keys(Keys.BACKSPACE)
departure_input.send_keys(departure_city)
time.sleep(1)
departure_input.send_keys(Keys.ENTER)

# Fill destination city
destination_input = driver.find_element(By.XPATH, "//input[@aria-label='Flight destination input']")
destination_input.click()
time.sleep(1)
destination_input.send_keys(Keys.CONTROL + "a")
destination_input.send_keys(Keys.BACKSPACE)
destination_input.send_keys(destination_city)
time.sleep(1)
destination_input.send_keys(Keys.ENTER)

# (Optional: Dates are trickier; we can skip dates for now or add them later)

# Wait and let kayak load suggestions & auto search
time.sleep(10)

# Get first few prices (example scraping)
prices = driver.find_elements(By.XPATH, "//div[contains(@class, 'price-text')]")[:3]
for price in prices:
    print(price.text)


driver.quit()
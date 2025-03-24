from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Set options
options = Options()
options.add_argument("--headless")  # optional, remove if you want to see browser
options.add_argument("--window-size=1920,1080")
service = Service()  # assumes chromedriver in PATH

# Start driver
driver = webdriver.Chrome(service=service, options=options)

# Open kayak flight search page
url = "https://www.kayak.com/flights"
driver.get(url)
time.sleep(5)  # give it time to load

# Print page title
print(driver.title)

# Close for now
driver.quit()
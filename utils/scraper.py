from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



def fill_departure_city(driver,departure_city):
    departure_input = driver.find_element(By.XPATH, "//input[@aria-label='Flight origin input']")

    departure_input.click()
    time.sleep(2)

    departure_input.send_keys(Keys.CONTROL + "a")  # select all text
    departure_input.send_keys(Keys.BACKSPACE)
    departure_input.send_keys(Keys.BACKSPACE)
    departure_input.send_keys(Keys.BACKSPACE)

    departure_input.send_keys(departure_city)
    time.sleep(2)

    departure_input.send_keys(Keys.ENTER)
    time.sleep(5)




def fill_destination_city(driver,destination_city):
    destination_input = driver.find_element(By.XPATH, "//input[@aria-label='Flight destination input']")
    destination_input.click()
    time.sleep(2)
    destination_input.send_keys(Keys.CONTROL + "a")
    destination_input.send_keys(Keys.BACKSPACE)
    destination_input.send_keys(Keys.BACKSPACE)
    destination_input.send_keys(Keys.BACKSPACE)
    destination_input.send_keys(destination_city)
    time.sleep(2)
    destination_input.send_keys(Keys.ENTER)
    time.sleep(5)


def fill_departure_date(driver,departure_date):
    departure_date_xpath = f"//div[@role='button' and contains(@aria-label, '{departure_date}')]"

    departure_date_element = driver.find_element(By.XPATH, departure_date_xpath)
    departure_date_element.click()
    time.sleep(2)

def fill_return_date(driver,return_date):
    return_date_xpath = f"//div[@role='button' and contains(@aria-label, '{return_date}')]"

    return_date_element = driver.find_element(By.XPATH, return_date_xpath)
    return_date_element.click()
    time.sleep(2)




def search_flights(driver):
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Search']"))
    )
    search_button.click()
    time.sleep(10)
    


def select_new_tab_if_redirected(driver):
    # Store the current window handle
    main_window = driver.current_window_handle

    # After clicking search button, wait a second or two for new tab to open
    time.sleep(2)

    # Get all open windows/tabs
    all_windows = driver.window_handles

    # Switch to the new tab (the one that is not the main window)
    for window in all_windows:
        if window != main_window:
            driver.switch_to.window(window)
            break

def load_more(driver):
    
    
    try:
        load_more = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Show more results')]"))
        )
        driver.execute_script("arguments[0].scrollIntoView();", load_more) #Scroll the page so that arguments[0] (the element you pass i.e load_more) comes into the visible part of the window.
        time.sleep(1)
        load_more.click()
        
        time.sleep(5)  # Allow time for new results to load
    except:
        print("No more 'Show more results' button found.")
        
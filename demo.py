# %%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time 


# %%
options = Options()
options.add_argument("--start-maximized")

service = Service()

driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.kayak.com/flights")
time.sleep(5)
print(driver.title)


# %%
departure_city = "New York"
destination_city = "London"
departure_date = "April 4, 2025"
return_date = "April 5, 2025"

# %%


# %% [markdown]
# # Fill departure city

# %%

departure_input = driver.find_element(By.XPATH, "//input[@aria-label='Flight origin input']")
departure_input

# %%
departure_input.click()
time.sleep(2)

# %%
departure_input.send_keys(Keys.CONTROL + "a")  # select all text
departure_input.send_keys(Keys.BACKSPACE)
departure_input.send_keys(Keys.BACKSPACE)
departure_input.send_keys(Keys.BACKSPACE)

# %%
departure_input.send_keys(departure_city)
time.sleep(2)

# %%
departure_input.send_keys(Keys.ENTER)

# %% [markdown]
# # Fill destination city

# %%
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

# %%
departure_date_xpath = f"//div[@role='button' and contains(@aria-label, '{departure_date}')]"

departure_date_element = driver.find_element(By.XPATH, departure_date_xpath)
departure_date_element.click()

# %%
departure_date_xpath = f"//div[@role='button' and contains(@aria-label, '{return_date}')]"

departure_date_element = driver.find_element(By.XPATH, departure_date_xpath)
departure_date_element.click()
time.sleep(2)

# %%
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Search']"))
)
search_button.click()
time.sleep(10)

# %%
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

# %%
flights = driver.find_elements(By.XPATH, "//div[contains(@id,'flight-results-list-wrapper')]")

flights

# %%
len(flights)

# %%
'''price = flights[0].find_element(By.XPATH, ".//span[contains(@class,'price-text')]").text'''

# %%
flight_combos = driver.find_elements(By.XPATH, "//ol[contains(@class, 'hJSA-list')]")
len(flight_combos)

# %%
flight_combos = driver.find_elements(By.XPATH, "//ol[contains(@class, 'hJSA-list')]")
len(flight_combos)


# %%
load_more_clicks = 5
for i in range(load_more_clicks):
    try:
        load_more = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Show more results')]"))
        )
        driver.execute_script("arguments[0].scrollIntoView();", load_more)
        time.sleep(1)
        load_more.click()
        print(f"Clicked Load More {i+1} times")
        time.sleep(5)  # Allow time for new results to load
    except:
        print("No more 'Show more results' button found.")
        break

# %%
flight_results = driver.find_elements(By.XPATH, "//div[contains(@class, 'nrc6-wrapper')]")
len(flight_results)

# %%
from bs4 import BeautifulSoup
for i,combo in enumerate(flight_results):
    
    flights = combo.find_elements(By.XPATH, ".//li[contains(@class,'hJSA-item')]")
    '''
    for i, el in enumerate(flights, start=1):
        html_code = el.get_attribute('outerHTML')
        soup = BeautifulSoup(html_code, 'html.parser')
        pretty_html = soup.prettify()
        print(f"\nElement {i}:\n{pretty_html}\n{'='*40}")
    '''
    print(i)
    price=combo.find_elements(By.XPATH, ".//div[contains(@class,'price-section')]//div[contains(@class, 'price-text')]")[0].text
    print(price)
    for flight in flights:
        # departure & arrival times
        times = flight.find_elements(
            By.XPATH, ".//div[contains(@class,'VY2U')]//span[contains(text(), 'am') or contains(text(), 'pm')]"
        )
        dep_time = times[0].text.strip().split('+')[0].strip()
        arr_time = times[1].text.strip().split('+')[0].strip()
        print(dep_time,arr_time)
        # airline
       
        airline = flight.find_element(
            By.XPATH, ".//div[contains(@class,'c_cgF') and not(.//span)]"
        ).text.strip()

        # duration
        duration = flight.find_element(
            By.XPATH, ".//div[contains(text(),'h') and contains(text(),'m')]"
        ).text.strip()

        # origin and destination airports
        airports = flight.find_elements(
            By.XPATH, ".//div[contains(@class,'EFvI')]//div[contains(@class,'c_cgF c_cgF-mod-variant-default')]"
        )
        origin = airports[0].get_attribute("title")
        destination = airports[1].get_attribute("title")
        
        '''for i, el in enumerate(airports, start=1):
            html_code = el.get_attribute('outerHTML')
            soup = BeautifulSoup(html_code, 'html.parser')
            pretty_html = soup.prettify()
            print(f"\nElement {i}:\n{pretty_html}\n{'='*40}")'''

        print(f"Departure: {dep_time}, Arrival: {arr_time}, Airline: {airline}, Duration: {duration}")
        print(f"From: {origin}  -->  To: {destination}\n")
       

       

# %%
import pandas as pd
flight_data = []
for i, combo in enumerate(flight_results, start=1):
    flights = combo.find_elements(By.XPATH, ".//li[contains(@class,'hJSA-item')]")
    price = combo.find_elements(By.XPATH, ".//div[contains(@class,'price-section')]//div[contains(@class, 'price-text')]")[0].text

    if len(flights) == 2:
        # Outbound
        flight_out = flights[0]
        out_times = flight_out.find_elements(
            By.XPATH, ".//div[contains(@class,'VY2U')]//span[contains(text(), 'am') or contains(text(), 'pm')]"
        )
        out_dep_time = out_times[0].text.strip().split('+')[0].strip()
        out_arr_time = out_times[1].text.strip().split('+')[0].strip()
        out_airline = flight_out.find_element(
            By.XPATH, ".//div[contains(@class,'c_cgF') and not(.//span)]"
        ).text.strip()
        out_airports = flight_out.find_elements(
            By.XPATH, ".//div[contains(@class,'EFvI')]//div[contains(@class,'c_cgF c_cgF-mod-variant-default')]"
        )
        out_origin = out_airports[0].get_attribute("title")
        out_destination = out_airports[1].get_attribute("title")

        # Return
        flight_ret = flights[1]
        ret_times = flight_ret.find_elements(
            By.XPATH, ".//div[contains(@class,'VY2U')]//span[contains(text(), 'am') or contains(text(), 'pm')]"
        )
        ret_dep_time = ret_times[0].text.strip().split('+')[0].strip()
        ret_arr_time = ret_times[1].text.strip().split('+')[0].strip()
        ret_airline = flight_ret.find_element(
            By.XPATH, ".//div[contains(@class,'c_cgF') and not(.//span)]"
        ).text.strip()
        ret_airports = flight_ret.find_elements(
            By.XPATH, ".//div[contains(@class,'EFvI')]//div[contains(@class,'c_cgF c_cgF-mod-variant-default')]"
        )
        ret_origin = ret_airports[0].get_attribute("title")
        ret_destination = ret_airports[1].get_attribute("title")

        # Append to data list
        flight_data.append({
            "Index": i,
            "Airline Name": out_airline,
            "From": out_origin,
            "To": out_destination,
            "Departure": out_dep_time,
            "Arrival": out_arr_time,
            "Return Airline Name": ret_airline,
            "Return From": ret_origin,
            "Return To": ret_destination,
            "Return Departure": ret_dep_time,
            "Return Arrival": ret_arr_time,
            "Price": price
        })

# %%
flight_data

# %%
df = pd.DataFrame(flight_data)
df.to_csv("flights_output.csv", index=False)
print("✅ Saved to flights_output.csv!")

# %%


# %%


# %%


# %%


# %%




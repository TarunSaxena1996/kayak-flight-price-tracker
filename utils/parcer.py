from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def extract_data(driver):
    flight_results = driver.find_elements(By.XPATH, "//div[contains(@class, 'nrc6-wrapper')]")
    len(flight_results)

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
    return flight_data
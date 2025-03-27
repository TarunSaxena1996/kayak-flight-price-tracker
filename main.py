
from utils.browser import launch_browser
from utils.scraper import fill_departure_city, fill_destination_city, fill_departure_date, fill_return_date, search_flights,select_new_tab_if_redirected, load_more
from utils.parser import extract_data
from utils.save import save
from utils.notifier import notify
import time
import config

def main():
    print("lauching chrome")
    driver = launch_browser(headless=False)
    driver.get("https://www.kayak.com/flights")
    time.sleep(5)
    
    print("fill_departure_city")
    fill_departure_city(driver, config.departure_city)
    print("fill_destination_city")
    fill_destination_city(driver, config.destination_city)

    print("filling dates")
    fill_departure_date(driver, config.departure_date)
    fill_return_date(driver, config.return_date)

    print("searching flights")
    search_flights(driver)

    select_new_tab_if_redirected(driver)

    for i in range(5):

        load_more(driver)
        print("number of times loaded more:",i)

    flight_data= extract_data(driver)
    print("flight_data extracted")

    print("saving output to csv file to: output/flights_output.csv")
    save(flight_data)

    
    notify(driver,config.threshold_price)
    print("Sending you flight details via mail while cost is less than the set limit")









    time.sleep(50)
    #driver.quit()

if __name__ == "__main__":
    main()


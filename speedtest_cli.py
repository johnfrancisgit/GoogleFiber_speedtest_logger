import selenium
import docopt

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

def main():
    GFIBER_SPEEDTEST_URL = "http://speedtest.googlefiber.net" 

    driver = webdriver.PhantomJS(executable_path="/usr/local/bin/phantomjs")
    driver.get(GFIBER_SPEEDTEST_URL)
    run_test = driver.find_element_by_id("run-test")

    run_test.click()

    # Check if we're on the Google fiber network
    try:
        cf = driver.find_element_by_class_name("actionButton-confirmSpeedtest")
        cf.click()
    except selenium.common.exceptions.NoSuchElementException:
        # We're on the google fiber network
        pass
                                                                                                                                        # Landed directly on dashboard page
                                                                                                                                                    continue

                                                                                                                                                        # Run tests
                                                                                                                                                                output += check_not_loading(driver)
                                                                                                                                                                        output += check_weather_values(driver)

                                                                                                                                                                                # Check 6h forecast graphs - (driver, past_timesteps, future_timesteps)
                                                                                                                                                                                        output += check_weather_graphs(driver, 4, 6)


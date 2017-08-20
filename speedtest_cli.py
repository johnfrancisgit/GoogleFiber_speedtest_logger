import os
import selenium
import docopt
import ipdb

from time import sleep

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display


GFIBER_SPEEDTEST_URL = "http://speedtest.googlefiber.net" 


def init_virtual_display():
    display = Display(visible=0, size=(1920, 1080))
    display.start()
    return display


def init_driver():
    curdir = os.path.dirname(__file__)
    chromedriverdir = os.path.join(curdir, "venv/chromedriver-Linux64")

    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument('remote-debugging-port=9222')
    # chrome_options.add_argument('disable-gpu')
   
    try:
        # driver = webdriver.PhantomJS(executable_path="/usr/local/bin/phantomjs"])
        driver = webdriver.Chrome(chromedriverdir, 
                                  chrome_options=chrome_options)
    except selenium.common.exceptions.WebDriverException as e:
        print(e)
    return driver


def run_test(driver):
    driver.get(GFIBER_SPEEDTEST_URL)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "run-test"))
    )

    run_test = driver.find_element_by_id("run-test")
    run_test.click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'actionButton-confirmSpeedtest'))
    )
    # Check if we're on the Google fiber network
    try:
        cf = driver.find_element_by_class_name("actionButton-confirmSpeedtest")
        cf.click()
    except selenium.common.exceptions.NoSuchElementException:
        # We're on the google fiber network
        print("You're on the google fiber network") 

    # Wait until the speedtest has completed
    element = WebDriverWait(driver, 60).until(
        EC.text_to_be_present_in_element((By.ID, "view32"), "Done")
    )

    download = driver.find_element_by_name("downloadSpeedMbps").text
    upload = driver.find_element_by_name("uploadSpeedMbps").text
    ping = driver.find_element_by_name("ping").text
    print("Download speed: {} \nUpload speed: {} \nPing: {}".format(download,
                                                                    upload,
                                                                    ping))
    driver.close()
if __name__ == "__main__":
    display = init_virtual_display()
    driver = init_driver()
    run_test(driver)
    driver.quit()
    display.stop()

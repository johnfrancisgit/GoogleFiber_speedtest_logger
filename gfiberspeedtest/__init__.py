from .speedtest_cli import (init_virtual_display, init_driver, scrape)


def run():
    display = init_virtual_display()
    driver = init_driver()
    results = scrape(driver)
    driver.quit()
    display.stop()
    return results

def cli():
    print("Running speedtest")
    result = run()
    result_str = "Download speed: {}Mbps \nUpload speed: {}Mbps \nPing: {}ms"
    print(result_str.format(result["download"], result["upload"],
                                   result["ping"]))

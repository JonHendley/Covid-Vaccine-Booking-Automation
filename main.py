import time
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

loop = True

service = Service('Path Placeholder')  # path to chrome driver
service.start()
driver = webdriver.Remote(service.service_url)
# Open the website
driver.get('https://vaccine.covaxonbooking.ca/manage')
time.sleep(1)
driver.find_element_by_xpath("//*[@id='cancelPage-phone']").send_keys('Phone Number Placeholder')  # Phone number
driver.find_element_by_id('cancelPage-code').send_keys('Booking Confirmation Code Placeholder')  # Booking Confirmation Code
driver.find_element_by_xpath("//*[@id='root']/div/main/div/form/button").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='root']/div/main/div/div[2]/div[1]/div/div[1]/button").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='root']/div/main/div/div[1]/p/a").click()
driver.find_element_by_xpath("//*[@id='location-search-input']").send_keys('Postal Code Placeholder')  # Postal Code
driver.find_element_by_xpath("//*[@id='root']/div/main/div/div[4]/button[1]").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='root']/div/main/div[1]/div/div[2]/div[2]/button").click()  # Pick Vaccination
# Clinic in list
while loop:
    if len(driver.find_elements_by_xpath("//*[@id='root']/div/main/div/div[2]/div[3]/div/div[2]/h3")) != 0:  # Date
        # available
        driver.find_element_by_xpath("//*[@id='root']/div/main/div/div[2]/div[3]/div/div[2]/div/div/button").click()
        time.sleep(2)
        if len(driver.find_elements_by_xpath("// *[ @ id = 'root'] / div / main / div / div[1] / div[2]")) != 0:
            driver.find_element_by_xpath("//*[@id='root']/div/main/div/div[3]/div/button[1]").click()
            loop = False
        else:
            driver.find_element_by_xpath(
                "//*[@id='root']/div/main/div/div[2]/div[3]/div/div/div/div/div/div[2]/div[1]/div[1]/button").click()
            time.sleep(2)
            driver.find_element_by_xpath(
                "//*[@id='root']/div/main/div/div[2]/div[3]/div/div/div/div/div/div[2]/div[1]/div[2]/button").click()
    else:
        time.sleep(2)
        driver.find_element_by_xpath(
            "//*[@id='root']/div/main/div/div[2]/div[3]/div/div/div/div/div/div[2]/div[1]/div[1]/button").click()
        time.sleep(1)
        driver.find_element_by_xpath(
            "//*[@id='root']/div/main/div/div[2]/div[3]/div/div/div/div/div/div[2]/div[1]/div[2]/button").click()

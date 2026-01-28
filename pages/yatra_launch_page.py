import datetime
import logging
import time

from selenium.common import StaleElementReferenceException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_driver import BaseDriver
from utilities.utils import Utils


class Launch_Page(BaseDriver):
    log = Utils.custom_logger(loglevel=logging.WARNING)
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

       # locators
    DEPARTURE_FIELD = "//input[@id='BE_flight_origin_city']"
    GOING_TO_FIELD = "//li[@class='w225']//input[@id='BE_flight_arrival_city']"
    GOING_SEARCH_RESULTS = "//div[@class='viewport']//div/li"
    DEPARTURE_DATE = "//div[ @id='monthWrapper']//tbody//td[@class!='inActiveTD']"


    def getdeparturefield(self):
        return self.driver.find_element(By.XPATH, self.DEPARTURE_FIELD)

    def goingtofield(self):
        return self.driver.find_element(By.XPATH, self.GOING_TO_FIELD)

    def goingsearchresults(self):
        return self.driver.find_elements(By.XPATH, self.GOING_SEARCH_RESULTS)

    def getdeparturedate(self):
        return self.driver.find_elements(By.XPATH, self.DEPARTURE_DATE)

    def enterdepartFromLocation(self, departlocation):
        self.getdeparturefield().click()
        self.getdeparturefield().send_keys(departlocation)
        self.getdeparturefield().send_keys(Keys.ENTER)
        time.sleep(4)
        self.log.info("inside depart location")

    def entergoingToLocation(self, goinglocation):
        self.goingtofield().click()
        self.goingtofield().send_keys(goinglocation)
        time.sleep(3)
        going_to=self.goingsearchresults()
        print(len(going_to))
        self.log.info("inside going to location")

        for city in going_to:
            if goinglocation in city.text:
                city.click()
                time.sleep(4)
                break

    # def selectdeparturedate(self, selectdate):
    #
    #     for date in self.getdeparturedate():
    #         if date.get_attribute("data-date") == selectdate:
    #             date.click()
    #             time.sleep(4)
    #             break

    # def clicksearch(self):
    #     self.driver.find_element(By.XPATH, "//input[@id='BE_flight_flsearch_btn']").click()
    #     time.sleep(4)
    #
    #   # wait for search results
    #     wait = WebDriverWait(self.driver, 30)
    #
    #
    #     wait.until(
    #         EC.visibility_of_all_elements_located(
    #             (By.XPATH, "//p[@class='font-lightgrey bold' and (normalize-space()='Non Stop' or normalize-space()='1' or normalize-space()='2')]")))
    #
    #     print("Total 1-stop flights:", len(all_stop))

    def getdeparturedate(self, departuredate):

        wait = WebDriverWait(self.driver, 15)
        # Open calendar
        self.getdeparturedate.click()

        target_date = datetime.strptime(departuredate, "%d/%m/%Y")
        target_month_year = target_date.strftime("%B %Y")  # February 2026
        target_day = target_date.strftime("%d").lstrip("0")
        while True:
            month_year = wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//span[@class='month-title']")
                )                ).text

            if month_year == target_month_year:
                break

                # Click next month
                self.driver.find_element(By.XPATH, "//span[@class='next-month']").click()

            # Select the day
        day_element = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//td[not(contains(@class,'inActiveTD'))]/span[text()='{target_day}']")
                )
            )
        day_element.click()


    def searchFlights(self, departlocation, goinglocation, departuredate):
        self.enterdepartFromLocation(departlocation)
        self.entergoingToLocation(goinglocation)
        self.getdeparturedate(departuredate)
        self.clicksearch()


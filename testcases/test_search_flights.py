import pytest
import csv
import os
from pages.search_flights_results_page import SearchFlightsResults
from pages.yatra_launch_page import Launch_Page


def load_test_data_from_csv():
    file_path = os.path.join(os.path.dirname(__file__), "..\\testdata\\testcsv.csv")

    test_data = []
    with open(file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            test_data.append(
                (row["goingfrom"], row["goingto"], row["date"])
            )
    return test_data


@pytest.mark.usefixtures("setup")
class Testsearchflights:

    @pytest.mark.parametrize(
        "goingfrom, goingto, date",
        load_test_data_from_csv()
    )
    def test_search_flights(self, goingfrom, goingto, date):

        lp = Launch_Page(self.driver)
        lp.searchFlights(goingfrom, goingto, date)
        lp.scroll_page()

        sf = SearchFlightsResults(self.driver)
        sf.filter_results()


'''
import os
import pytest
import pandas as pd
from pages.search_flights_results_page import SearchFlightsResults
from pages.yatra_launch_page import Launch_Page

def load_test_data_from_excel():
    # Construct path relative to this script
    file_path = os.path.join(os.path.dirname(__file__), "..\\testdata\\tax cal.xlsx")
    df = pd.read_excel(file_path, engine="openpyxl")
    return [(row['goingfrom'], row['goingto'], row['date']) for index, row in df.iterrows()]

@pytest.mark.usefixtures("setup")
class Testsearchflights:

    @pytest.mark.parametrize(
        "goingfrom, goingto, date",
        load_test_data_from_excel()
    )
    def test_search_flights(self, goingfrom, goingto, date):
        lp = Launch_Page(self.driver)
        lp.searchFlights(goingfrom, goingto, date)
        lp.scroll_page()

        sf = SearchFlightsResults(self.driver)
        sf.filter_results()
'''

'''
import pytest
import yaml
from pages.search_flights_results_page import SearchFlightsResults
from pages.yatra_launch_page import Launch_Page


def load_test_data():
    with open("testdata/testdatayaml.yaml") as f:
        data = yaml.safe_load(f)
    return [(d["goingfrom"], d["goingto"], d["date"]) for d in data]


@pytest.mark.usefixtures("setup")
class Testsearchflights:

    @pytest.mark.parametrize(
        "goingfrom, goingto, date",
        load_test_data()
    )
    def test_search_flights(self, goingfrom, goingto, date):

        lp = Launch_Page(self.driver)
        lp.searchFlights(goingfrom, goingto, date)
        lp.scroll_page()

        sf = SearchFlightsResults(self.driver)
        sf.filter_results()


'''

'''
import pytest
from pages.search_flights_results_page import SearchFlightsResults
from pages.yatra_launch_page import Launch_Page


@pytest.mark.usefixtures("setup")
class Testsearchflights:

    @pytest.mark.parametrize("goingfrom, goingto, date", [
        ("New Delhi", "New York", "28/02/2026")
    ])
    def test_search_flights(self, goingfrom, goingto, date):
        lp = Launch_Page(self.driver)
        lp.searchFlights(goingfrom, goingto, date)
        lp.scroll_page()

        sf = SearchFlightsResults(self.driver)
        sf.filter_results()

'''
'''
import pytest
from pages.search_flights_results_page import SearchFlightsResults
from pages.yatra_launch_page import Launch_Page
from ddt import ddt, data, unpack

@pytest.mark.usefixtures("setup")
@ddt
class Testsearchflights:
    @data("New Delhi", "New York","28/02/2026")
    @unpack
    def test_search_flights(self, goingfrom ,goingto ,date):

        # launching browser and opening travel website
        # select going from
        lp = Launch_Page(self.driver)

        # lp.departfrom("New Delhi")
        lp.searchFlights(goingfrom, goingto, date)

        # lp.enterdepartFromLocation("New Delhi")

        # select going to
        # lp.goingto("New York")
        # lp.entergoingToLocation("New York")

        # select travel date
        # lp.selectdeparturedate("28/01/2026")
        # lp.selectdate("28/01/2026")

        #search flight
        # lp.clicksearch()

        #scroll search page
        lp.scroll_page()

        #select filter stop 1
        sf=SearchFlightsResults(self.driver)
        sf.filter_results()

'''


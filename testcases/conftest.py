import pytest
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# ---------- FIX 1: GLOBAL DRIVER STORE ----------
@pytest.fixture(scope="class")
def setup(request):

    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.get("https://www.yatra.com/offer/details/icici-bank-offers")
    driver.maximize_window()

    request.cls.driver = driver

    # ✅ store driver where hook can access it
    request.session.driver = driver

    yield
    driver.quit()


# ---------- FIX 2: SCREENSHOT HOOK ----------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        # ✅ driver from session (NOT item)
        driver = getattr(item.session, "driver", None)
        if driver is None:
            return

        pytest_html = item.config.pluginmanager.getplugin("html")
        if pytest_html is None:
            return

        screenshots_dir = os.path.join(
            item.config.rootpath, "reports", "screenshots"
        )
        os.makedirs(screenshots_dir, exist_ok=True)

        file_name = report.nodeid.replace("::", "_") + "_" + str(int(time.time())) + ".png"
        file_path = os.path.join(screenshots_dir, file_name)

        driver.save_screenshot(file_path)

        extra = getattr(report, "extras", [])
        extra.append(pytest_html.extras.image(file_path))
        report.extras = extra


def pytest_html_report_title(report):
    report.title = "Flight Automation Test Report"



# import pytest
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
#
# #url https://www.yatra.com/offer/details/icici-bank-offers
#
#
# @pytest.fixture(autouse=True)
# def setup(request, browser):
#     if browser == "chrome":
#         driver = webdriver.Chrome(ChromeDriverManager().install())
#     elif browser == "firefox":
#         driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#     elif browser == "edge":
#         driver = webdriver.Edge(EdgeChromiumDriverManager().install())
#     driver.get(url)
#     driver.maximize_window()
#     request.cls.driver = driver
#
#     yield
#     driver.close()
#
# def pytest_addoption(parser):
#     parser.addoption("--browser")
#     parser.addoption("--url")
#
# @pytest.fixture(scope="class", autouse=True)
# def browser(request):
#     return request.config.getoption("--browser")
#
# @pytest.fixture(scope="class", autouse=True)
# def url(request):
#     return request.config.getoption("--url")


# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from selenium.webdriver.edge.service import Service as EdgeService
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.core import driver
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from datetime import datetime
#
# @pytest.fixture(scope="class")
# def setup(request):
#
#     # Read browser and URL from command line
#     browser_choice = request.config.getoption("--browser", default="chrome").lower()
#     test_url = request.config.getoption("--url", default="https://www.yatra.com/offer/details/icici-bank-offers")
#
#     if browser_choice == "chrome":
#         service = ChromeService(ChromeDriverManager().install())
#         driver = webdriver.Chrome(service=service)
#     elif browser_choice == "firefox":
#         service = FirefoxService(GeckoDriverManager().install())
#         driver = webdriver.Firefox(service=service)
#     elif browser_choice == "edge":
#         service = EdgeService(EdgeChromiumDriverManager().install())
#         driver = webdriver.Edge(service=service)
#     else:
#         raise Exception(f"Browser '{browser_choice}' is not supported")
#
#     driver.get(test_url)
#     driver.maximize_window()
#     request.cls.driver = driver
#     request.node.driver = driver
#
#     yield
#     driver.quit()
#
#
# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on")
#     parser.addoption("--url", action="store", default="https://www.yatra.com/offer/details/icici-bank-offers", help="URL to test")



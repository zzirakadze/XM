import logging
import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def setup_chrome(headless: bool) -> webdriver.Chrome:
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    if headless:
        chrome_options.add_argument("--headless")
    return webdriver.Chrome(
        executable_path=ChromeDriverManager().install(), options=chrome_options
    )


def setup_firefox(headless: bool) -> webdriver.Firefox:
    firefox_options = FirefoxOptions()
    if headless:
        firefox_options.headless = True
    driver = webdriver.Firefox(
        executable_path=GeckoDriverManager().install(), options=firefox_options
    )
    driver.maximize_window()
    return driver


DRIVER_SETUP_FUNCTIONS = {"chrome": setup_chrome, "firefox": setup_firefox}


@pytest.fixture(scope="session")
def driver_instance(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    headless = request.config.getoption("--headless").lower() == "true"

    if browser not in DRIVER_SETUP_FUNCTIONS:
        raise ValueError(f"Unsupported browser: {browser}")

    driver_setup_function = DRIVER_SETUP_FUNCTIONS[browser]
    driver = driver_setup_function(headless)

    logging.info(
        f"Browser: {browser} execution started on {url} with headless mode: {headless} at {os.getcwd()}, time: {os.times()}"
    )
    driver.get(url)
    request.addfinalizer(driver.quit)
    logging.info(
        f"Browser: {browser} execution finished on {url} with headless mode: {headless} at {os.getcwd()}, time: {os.times()}"
    )

    return driver


def pytest_addoption(parser) -> None:
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Choose the browser to run the tests on",
    )
    parser.addoption(
        "--url",
        action="store",
        default="https://www.xm.com/",
        help="Choose the url to run the tests on",
    )
    parser.addoption(
        "--headless",
        action="store",
        default="false",
        help="Choose the headless mode to run the tests on",
    )

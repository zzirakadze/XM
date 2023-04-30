import pytest

from pages.economic_calendar_page import EconomicCalendarPage
from pages.home_page import HomePage
from pages.research_and_education import ResearchAndEducationPage


@pytest.fixture(scope="session")
def home_page(driver_instance):
    return HomePage(driver_instance)


@pytest.fixture(scope="session")
def res_and_edu_page(driver_instance):
    return ResearchAndEducationPage(driver_instance)


@pytest.fixture(scope="session")
def economic_calendar_page(driver_instance):
    return EconomicCalendarPage(driver_instance)

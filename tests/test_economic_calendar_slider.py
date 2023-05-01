import pytest
from zzassertions.assertions import assertTrue, assertEquals
from utils.date_time_calculator import DateGenerator


class TestEconomicCalendarSlider:
    time = DateGenerator()

    @pytest.mark.parametrize(
        "index, expected_date",
        [
            (1, f"{time.get_today()}"),
            (2, f"{time.get_tomorrow()}"),
            (4, f"{time.get_next_week()}"),
            (6, f"{time.get_next_month()}"),
        ],
    )
    def test_economic_calendar_slider(
        self,
        driver_instance,
        home_page,
        res_and_edu_page,
        economic_calendar_page,
        index,
        expected_date,
    ) -> None:
        # navigate to economic calendar
        home_page.click_research_and_education()
        assertTrue(res_and_edu_page.is_present())
        res_and_edu_page.move_to_economic_calendar()
        assertTrue(economic_calendar_page.is_present())

        # move slider and assert date
        economic_calendar_page.move_slider(index)
        actual_date = economic_calendar_page.get_calendar_date()
        assertEquals(actual_date, expected_date)

from zzassertions.assertions import assertTrue


class TestEconomicCalendarSlider:

    def test_economic_calendar_slider(
        self, driver_instance, home_page, res_and_edu_page, economic_calendar_page
    ) -> None:

        # navigate to economic calendar
        home_page.click_research_and_education()
        assertTrue(res_and_edu_page.is_present())
        res_and_edu_page.move_to_economic_calendar()
        assertTrue(economic_calendar_page.is_present())

        # move slider to 1
        economic_calendar_page.click_slider_element(2)

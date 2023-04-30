from selenium.webdriver.common.by import By
from utils.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
import time


class EconomicCalendarPage(BasePage):
    """
    EconomicCalendarPage class provides functions for interacting with the Economic Calendar page.
    """
    SLIDER = (By.XPATH, '//mat-slider')
    SLIDER_THUMB = (By.XPATH, '//mat-slider//div[contains(@class, "mat-slider-thumb")]')

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def is_present(self) -> bool:
        try:
            self.switch_to_iframe()
            self.find_element(self.SLIDER)
            return True
        except Exception as e:
            self.logger.error(
                f"An error occurred while validating Economic Calendar page: {e}"
            )
            return False

    def move_slider(self, index: int) -> None:
        """
        Move the slider to the specified index
        Using the index, calculate the position to move the slider

        :param index:
        :return None:
        """
        slider = self.find_element(self.SLIDER)
        slider_thumb = self.find_element(self.SLIDER_THUMB)
        slider_width = slider.size["width"]
        step_size = slider_width / 6  # Since there are 6 positions

        # Calculate the position to move the slider
        move_position = step_size * index

        # Create action chain to move the slider using drag and drop
        actions = ActionChains(self.driver)
        actions.drag_and_drop_by_offset(slider_thumb, move_position, 0).perform()

        # Wait for the slider to settle
        time.sleep(1)

        # Print the position of the slider thumb
        slider_thumb_location = slider_thumb.location
        self.logger.info(f"Slider thumb location: {slider_thumb_location}")

    def click_slider_element(self, index: int) -> None:
        self.move_slider(index)

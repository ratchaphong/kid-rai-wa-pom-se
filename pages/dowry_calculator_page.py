from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class DowryCalculatorPage(BasePage):
    BRIDE_PRICE_INPUT = (By.ID, 'womanSalary')
    BRIDE_YEARS_INPUT = (By.ID, 'womanYears')
    BRIDE_FAM_WEALTH_RICH_INPUT = (By.XPATH, "//input[@type='radio' and @name='woman-fam-wealth' and @value='1.2']")
    BRIDE_FAM_WEALTH_MID_INPUT = (By.XPATH, "//input[@type='radio' and @name='woman-fam-wealth' and @value='1']")
    BRIDE_FAM_WEALTH_POOR_INPUT = (By.XPATH, "//input[@type='radio' and @name='woman-fam-wealth' and @value='0.5']")
    BRIDE_LOCATION_BKK_INPUT = (By.ID, 'liveInBkk')
    BRIDE_LOCATION_OTHERS_INPUT = (By.ID, 'liveInOthers')

    GROOM_PRICE_INPUT = (By.ID, 'manSalary')
    GROOM_YEARS_INPUT = (By.ID, 'manYears')
    GROOM_FAM_WEALTH_RICH_INPUT = (By.XPATH, "//input[@type='radio' and @name='man-fam-wealth' and @value='1.5']")
    GROOM_FAM_WEALTH_MID_INPUT = (By.XPATH, "//input[@type='radio' and @name='man-fam-wealth' and @value='1']")
    GROOM_FAM_WEALTH_POOR_INPUT = (By.XPATH, "//input[@type='radio' and @name='man-fam-wealth' and @value='0.25']")

    EDUCATION_DROPDOWN = (By.ID, 'education')
    GREED_MULTIPLIER_SLIDER = (By.ID, 'greedMultiplyer')

    MIN_RESULT_TEXT = (By.ID, 'answer1')
    MAX_RESULT_TEXT = (By.ID, 'answer2')
    CALCULATE_BUTTON = (By.XPATH, "//div[contains(text(), 'คำนวณ')]")

    def enter_bride_info(self, price, years, wealth, live, education):
        self.clear_text(*self.BRIDE_PRICE_INPUT)
        self.type_text(price, *self.BRIDE_PRICE_INPUT)
        self.clear_text(*self.BRIDE_YEARS_INPUT)
        self.type_text(years, *self.BRIDE_YEARS_INPUT)
        if (wealth == "rich"):
            self.select_radio_button(*self.BRIDE_FAM_WEALTH_RICH_INPUT)
        elif (wealth == "mid"):
            self.select_radio_button(*self.BRIDE_FAM_WEALTH_MID_INPUT)
        else:
            # self.select_radio_button(*self.BRIDE_FAM_WEALTH_POOR_INPUT)
            self.wait_and_click(*self.BRIDE_FAM_WEALTH_POOR_INPUT)

        if (live == 'bkk'):
            self.wait_and_click(*self.BRIDE_LOCATION_BKK_INPUT)
        else:
            self.wait_and_click(*self.BRIDE_LOCATION_OTHERS_INPUT)

        self.select_dropdown_option_by_value(education, *self.EDUCATION_DROPDOWN)

    def enter_groom_info(self, price, years, wealth):
        self.clear_text(*self.GROOM_PRICE_INPUT)
        self.type_text(price, *self.GROOM_PRICE_INPUT)
        self.clear_text(*self.GROOM_YEARS_INPUT)
        self.type_text(years, *self.GROOM_YEARS_INPUT)
        if (wealth == "rich"):
            self.select_radio_button(*self.GROOM_FAM_WEALTH_RICH_INPUT)
        elif (wealth == "mid"):
            self.select_radio_button(*self.GROOM_FAM_WEALTH_MID_INPUT)
        else:
            # self.select_radio_button(*self.GROOM_FAM_WEALTH_POOR_INPUT)
            self.wait_and_click(*self.GROOM_FAM_WEALTH_POOR_INPUT)

    def enter_greed_number(self, value):
        self.select_range_input(value, *self.GREED_MULTIPLIER_SLIDER)

    def click_calculate(self):
        # self.click(*self.CALCULATE_BUTTON)
        self.wait_and_click(*self.CALCULATE_BUTTON)

    def get_result(self):
        min = self.find_element(*self.MIN_RESULT_TEXT).text
        max = self.find_element(*self.MAX_RESULT_TEXT).text
        return min + " - " + max + " บาท"

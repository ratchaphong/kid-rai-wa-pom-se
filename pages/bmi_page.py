from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class BMIPage(BasePage):
    HEIGHT_INPUT = (By.ID, 'height')
    WEIGHT_INPUT = (By.ID, 'weight')
    CALCULATE_BUTTON = (By.XPATH, "//input[@value='คำนวณ' and @type='button']")
    RESULT_TEXT = (By.ID, 'result')
    BMI_LEVEL_TEXT = (By.ID, 'bmiLevel')

    def enter_height(self, height):
        self.type_text(height, *self.HEIGHT_INPUT)

    def enter_weight(self, weight):
        self.type_text(weight, *self.WEIGHT_INPUT)

    def click_calculate(self):
        self.click(*self.CALCULATE_BUTTON)

    def get_result(self):
        result = self.find_element(*self.RESULT_TEXT).text
        bmiLevel = self.find_element(*self.BMI_LEVEL_TEXT).text
        return { result, bmiLevel }

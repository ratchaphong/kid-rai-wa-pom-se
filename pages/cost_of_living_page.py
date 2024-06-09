from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CostOfLivingPage(BasePage):
    CITY_INPUT = (By.ID, 'city')
    SALARY_INPUT = (By.ID, 'salary')
    CALCULATE_BUTTON = (By.XPATH, "//button[contains(text(), 'Calculate')]")
    RESULT_TEXT = (By.ID, 'result')

    def enter_city(self, city):
        self.type_text(city, *self.CITY_INPUT)

    def enter_salary(self, salary):
        self.type_text(salary, *self.SALARY_INPUT)

    def click_calculate(self):
        self.click(*self.CALCULATE_BUTTON)

    def get_result(self):
        return self.find_element(*self.RESULT_TEXT).text

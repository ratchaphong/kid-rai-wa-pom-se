from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):
    COST_OF_LIVING_LINK = "https://kidhaina.com/costofliving.html"
    COST_OF_LIVING_LINK_MENU = (By.CSS_SELECTOR, '.box.menu-box[href="costofliving.html"]')
    BMI_LINK = "https://kidhaina.com/bmi.html"
    BMI_LINK_MENU = (By.CSS_SELECTOR, '.box.menu-box[href="bmi.html"]')
    DOWRY_LINK="https://kidhaina.com/dowrycalculator.html"
    DOWRY_LINK_MENU = (By.CSS_SELECTOR, '.box.menu-box[href="dowrycalculator.html"]')

    def go_to_dowry_calculator(self):
        # self.click(By.LINK_TEXT, 'Dowry Calculator')
        self.click(*self.DOWRY_LINK_MENU)
        self.wait.until(EC.url_to_be(self.DOWRY_LINK))
        print(self.driver.current_url)

    def go_to_bmi_calculator(self):
        # self.click(By.LINK_TEXT, 'BMI Calculator')
        self.click(*self.BMI_LINK_MENU)
        self.wait.until(EC.url_to_be(self.BMI_LINK))
        print(self.driver.current_url)

    def go_to_cost_of_living(self):
        # self.click(By.LINK_TEXT, 'Dowry Calculator')
        self.click(*self.COST_OF_LIVING_LINK_MENU)
        self.wait.until(EC.url_to_be(self.COST_OF_LIVING_LINK))
        print(self.driver.current_url)

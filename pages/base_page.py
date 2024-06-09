from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, *locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, *locator):
        element = self.find_element(*locator)
        element.click()

    def type_text(self, text, *locator):
        element = self.find_element(*locator)
        element.send_keys(text)

    def clear_text(self, *locator):
        element = self.find_element(*locator)
        element.clear()

    def select_radio_button(self, *locator):
        element = self.find_element(*locator)
        if not element.is_selected():
            element.click()
    
    def wait_and_click(self, *locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        if not element.is_displayed():
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def select_dropdown_option_by_value(self, value, *locator):
        select_element = self.find_element(*locator)
        select = Select(select_element)
        select.select_by_value(value)

    def select_dropdown_option_by_text(self, text, *locator):
        select_element = self.find_element(*locator)
        select = Select(select_element)
        select.select_by_visible_text(text)

    def select_range_input(self, value, *locator):
        element = self.find_element(*locator)
        self.driver.execute_script("arguments[0].value = arguments[1];", element, value)
        self.driver.execute_script("arguments[0].oninput();", element)
        # print(element.get_attribute("value"))

        
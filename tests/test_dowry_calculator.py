import unittest
from selenium import webdriver
from pages.dowry_calculator_page import DowryCalculatorPage

class DowryCalculatorTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://kidhaina.com/dowrycalculator.html')

    def test_dowry_calculation(self):
        page = DowryCalculatorPage(self.driver)
        page.enter_bride_info('0', '28', 'poor', 'others', '0.5')
        page.enter_groom_info('28000', '30', 'poor')
        page.enter_greed_number("3")
        page.click_calculate()
        
        result = page.get_result()
        print(result)  # พิมพ์ผลลัพธ์ทั้งหมดเพื่อดูว่าเกิดอะไรขึ้น
        self.assertTrue(result, "The result should not be empty")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

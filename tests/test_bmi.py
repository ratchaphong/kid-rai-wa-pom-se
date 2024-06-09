import unittest
from selenium import webdriver
from pages.bmi_page import BMIPage

class BMITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://kidhaina.com/bmi.html')

    def test_bmi_calculation(self):
        page = BMIPage(self.driver)
        page.enter_height('180')
        page.enter_weight('50')
        page.click_calculate()
        
        result = page.get_result()
        print(result) 
        # result = None
        self.assertTrue(result, "The result should not be empty")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

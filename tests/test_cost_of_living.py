import unittest
from selenium import webdriver
from pages.cost_of_living_page import CostOfLivingPage

class CostOfLivingTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://kidhaina.com/costofliving.html')

    def test_cost_of_living_calculation(self):
        page = CostOfLivingPage(self.driver)
        page.enter_city('Bangkok')
        page.enter_salary('50000')
        page.click_calculate()
        
        result = page.get_result()
        print(result)  # พิมพ์ผลลัพธ์ทั้งหมดเพื่อดูว่าเกิดอะไรขึ้น
        self.assertTrue(result, "The result should not be empty")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

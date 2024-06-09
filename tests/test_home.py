import unittest
from selenium import webdriver
from pages.home_page import HomePage

class HomePageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://kidhaina.com/')

    def test_navigate_to_dowry_calculator(self):
        home_page = HomePage(self.driver)
        home_page.go_to_dowry_calculator()
        self.assertIn('dowrycalculator.html', self.driver.current_url)
        print(self.driver.title)
        self.assertEqual("โปรแกรมคำนวนสินสอด โดย คิดให้นะ", self.driver.title)

    def test_navigate_to_bmi_calculator(self):
        home_page = HomePage(self.driver)
        home_page.go_to_bmi_calculator()
        self.assertIn('bmi.html', self.driver.current_url)
        print(self.driver.title)
        self.assertEqual("โปรแกรมคำนวณ ค่าดัชนีมวลกาย (BMI) โดย คิดให้นะ", self.driver.title)

    def test_navigate_to_cost_of_living(self):
        home_page = HomePage(self.driver)
        home_page.go_to_cost_of_living()
        self.assertIn('costofliving.html', self.driver.current_url)
        print(self.driver.title)
        self.assertEqual("โปรแกรมคำนวนค่าครองชีพ โดย คิดให้นะ", self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

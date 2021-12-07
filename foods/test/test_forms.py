from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# Integration test
class SearchFormTest(LiveServerTestCase):

	def test_search_navbar(self):
		selenium = webdriver.Chrome(executable_path="chromedriver.exe")
		selenium.maximize_window()
		# Choose your url to visit
		selenium.get('http://127.0.0.1:8000/')
		time.sleep(5)
		# find the elements you need to submit form
		product_name = selenium.find_element_by_name('searched')

		submit = selenium.find_element_by_class_name('btn-outline-primary')
		# populate the form with data
		product_name.send_keys('nutella')

		# submit form
		submit.send_keys(Keys.RETURN)
		time.sleep(5)
		# check result; page source looks at entire html document
		assert 'nutella' in selenium.page_source

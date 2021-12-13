import os
import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


class SearchFormTest(StaticLiveServerTestCase):

	@classmethod
	def setUpClass(cls):
		super().setUpClass()
		runOnTravis = 'TRAVIS' in os.environ 
		if runOnTravis:
			cls.selenium = WebDriver()
		else:
			specific_options=Options()
			specific_options.add_argument("--no-sandbox")
			specific_options.add_argument("--headless")
			specific_options.add_argument("--disable-dev-shm-usage")
			specific_options.add_argument("--disable-gpu")
			cls.selenium = WebDriver(options=specific_options)
		cls.selenium.implicitly_wait(10)
		
	@classmethod
	def tearDownClass(cls):
		cls.selenium.quit()
		super().tearDownClass()

	def test_search_navbar(self):
		self.selenium.maximize_window()
		# Choose your url to visit
		self.selenium.get('http://127.0.0.1:8000/')
		time.sleep(5)
		# find the elements you need to submit form
		product_name = self.selenium.find_element_by_name('searched')

		submit = self.selenium.find_element_by_id('navbarSearchbtn')
		# populate the form with data
		product_name.send_keys('nutella')

		# submit form
		submit.send_keys(Keys.RETURN)
		time.sleep(5)
		# check result; page source looks at entire html document
		assert 'nutella' in self.selenium.page_source
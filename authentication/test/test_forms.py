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
		self.selenium.get('http://127.0.0.1:8000/authentication/register/')
		time.sleep(2)
		# find the elements you need to submit form
		username = self.selenium.find_element_by_id('id_username')
		email = self.selenium.find_element_by_id('id_email')
		pswd1 = self.selenium.find_element_by_id('id_password1')
		pswd2 = self.selenium.find_element_by_id('id_password2')

		submit = self.selenium.find_element_by_id('valid-btn')
		# populate the form with data
		username.send_keys('maxime')
		email.send_keys('max@gmail.com')
		pswd1.send_keys('max12345.')
		pswd2.send_keys('max12345.')

		# submit form
		submit.send_keys(Keys.RETURN)
		time.sleep(5)
		# check result; page source looks at entire html document
		assert 'maxime' in self.selenium.page_source
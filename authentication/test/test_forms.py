import os
import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType

class SearchFormTest(StaticLiveServerTestCase):

	@classmethod
	def setUpClass(cls):
		super().setUpClass()
		runOnTravis = 'TRAVIS' in os.environ 
		if runOnTravis:
			specific_options=Options()
			specific_options.add_argument("--no-sandbox")
			specific_options.add_argument("--headless")
			specific_options.add_argument("start-maximized")
			specific_options.add_argument("--disable-dev-shm-usage")
			specific_options.add_argument("--disable-gpu")
			cls.selenium = WebDriver(options=specific_options)
		else:
			specific_options=Options()
			specific_options.add_argument("start-maximized")
			cls.selenium = WebDriver(options=specific_options)
		cls.selenium.implicitly_wait(10)

	@classmethod
	def tearDownClass(cls):
		cls.selenium.quit()
		super().tearDownClass()

	def test_search_navbar(self):

		# Choose your url to visit
		self.selenium.get('{}/authentication/register/'.format(self.live_server_url))
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
		name = self.selenium.find_element_by_name('username')
		pswd = self.selenium.find_element_by_name('password')
		valid = self.selenium.find_element_by_id('valid-text')
		# profile_name = self.selenium.find_element_by_css_selector('.text-white-75')
		name.send_keys('maxime')
		pswd.send_keys('max12345.')
		valid.send_keys(Keys.RETURN)
		# check result; page source looks at entire html document
		assert 'maxime' in self.selenium.page_source
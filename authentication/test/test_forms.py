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
		selenium.get('http://127.0.0.1:8000/authentication/register/')
		time.sleep(2)
		# find the elements you need to submit form
		username = selenium.find_element_by_id('id_username')
		email = selenium.find_element_by_id('id_email')
		pswd1 = selenium.find_element_by_id('id_password1')
		pswd2 = selenium.find_element_by_id('id_password2')

		submit = selenium.find_element_by_id('valid-btn')
		# populate the form with data
		username.send_keys('maxime')
		email.send_keys('max@gmail.com')
		pswd1.send_keys('max12345.')
		pswd2.send_keys('max12345.')

		# submit form
		submit.send_keys(Keys.RETURN)
		time.sleep(5)
		# check result; page source looks at entire html document
		assert 'maxime' in selenium.page_source

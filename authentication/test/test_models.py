from django.test import TestCase
from authentication.forms import RegisterForm


class RegisterModelsTest(TestCase):

	def test_register_form_field(self):
		name = 123
		email = 123
		form = RegisterForm(data={'username': name,
								  'email': email})
		self.assertFalse(form.is_valid())

	def test_register_form_field_empty(self):
		form = RegisterForm(data={'username': None,
								  'email': None, })
		self.assertIsNotNone(form.fields['username'])
		self.assertIsNotNone(form.fields['email'])


class LoginModelsTest(TestCase):

	def test_register_form_field_label(self):
		form = RegisterForm()
		self.assertTrue(
			form.fields['username'].label == None
			or form.fields['username'].label == "Nom d'utilisateur"
		)

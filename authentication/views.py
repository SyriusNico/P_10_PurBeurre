from django.views.generic import CreateView
from .forms import RegisterForm
from django.urls import reverse_lazy


class UserRegisterView(CreateView):
	form_class = RegisterForm
	template_name = 'registration/register.html'
	success_url = reverse_lazy('login')

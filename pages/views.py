from django.views.generic.base import TemplateView


class IndexView(TemplateView):
	template_name = 'pages/index.html'


class LegalView(TemplateView):
	template_name = 'pages/legal.html'

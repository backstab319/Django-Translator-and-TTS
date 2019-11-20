from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

class TandTTS(TemplateView):
    template_name = 'TandTTS/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class mainPage(TemplateView):
    template_name = 'DjangoTranslatorandTTS/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
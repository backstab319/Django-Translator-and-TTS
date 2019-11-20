from django.urls import path
from TandTTS.views import TandTTS


urlpatterns = [
    path('', TandTTS.as_view(), name='translator'),
]

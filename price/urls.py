from django.urls import path
from .views import exchange_page, home_page


urlpatterns = [
    path('cambio/', exchange_page, name='exchange-page'),
    path('', home_page, name='home-page')
]
from django.urls import path
from .views import exchange_page


urlpatterns = [
    path('cambio/', exchange_page, name='exchange_page')
]
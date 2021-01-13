from django.urls import path, include
from website import views

urlpatterns = [
   path('', views.home, name='home')
]
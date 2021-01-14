from django.urls import path, include
from website import views


urlpatterns = [
   path('', views.home, name='home'),
   path("post/<int:id>/", views.post_detail, name='post_detail'),
]
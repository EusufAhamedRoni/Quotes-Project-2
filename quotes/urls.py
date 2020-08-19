from django.urls import path
from quotes import views

urlpatterns = [
    path('', views.HomeView.as_view(), name = 'home'),
]

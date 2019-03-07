from django.urls import path, include
from start import views

urlpatterns = [
    path('', views.start , name="path"),
    path('portfolio/', views.portfolio , name="portfolio"),
]
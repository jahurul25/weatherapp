from django.urls import path
from weatherapp import views

urlpatterns = [
    path('city', views.City.as_view(), name='CityList'),
    path('getWeather/<str:city>', views.Weather.as_view(), name='getWeather'),

]
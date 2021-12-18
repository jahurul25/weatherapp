from rest_framework.views import APIView
from rest_framework.response import Response
from weatherapp import serializers
from weatherapp import models
import requests


# Create your views here.
#https://home.openweathermap.org/api_keys 

class Weather(APIView):
    serializer_class = serializers.WeacherSearchSerializer

    def get(self, request, city):
        try:
            urls = "https://api.openweathermap.org/data/2.5/weather?q="+str(city)+"&appid=b360f756f0bad59e0d0cf9362590b79c"
            getWeather = requests.get(urls).json()

            if "message" not in getWeather:
                cityWeather = {
                    "country": getWeather["sys"]["country"],
                    "city": getWeather["name"],
                    "temperature": round(float(getWeather["main"]["temp"]) - 273.15, 2),
                    "description": getWeather["weather"][0]["description"],
                    "icon": getWeather["weather"][0]["icon"]            
                } 
                return Response({ "result": "Weather data found", "weather": cityWeather }, status=200)
            else:
                return Response({ "result": "Weather data not found", "weather": [] }, status=200)
        except:
            return Response({ "result": "Error" }, status = 500)

class City(APIView):
    serializer_class = serializers.CitySerializer

    def get(self, request):
        try:
            city_list  = models.City.objects.filter(status=True).order_by("-id")
            
            if city_list:
                serializer   = self.serializer_class(city_list, many=True)
                return Response({"result": "City list found", "city_list": serializer.data}, status=200)
            else:
                return Response({"result": "City list not found", "city_list": []}, status=404)

        except Exception as ex:
            return Response({"result": "Error", "city_list": []}, status=500)

    def post(self, request):
        try: 
            city_name  = request.POST.get("city_name")  
            status     = True if request.POST.get("status") == 'true' else False
            
            models.City.objects.create(city_name = city_name, status = status) 
           
            return Response({ "result": "City added successful" }, status=200)
        except Exception as ex:
            return Response({ "result": "Error" }, status=500)

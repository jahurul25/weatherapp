from rest_framework import serializers
from weatherapp import models
 
class CitySerializer(serializers.ModelSerializer): 
    class Meta:
        model = models.City
        fields = ('id','city_name','status','created_date')

class WeacherSearchSerializer(serializers.ModelSerializer): 
    class Meta:
        model = models.City
        fields = ('id','city_name') 

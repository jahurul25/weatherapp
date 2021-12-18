from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class City(models.Model): 
    city_name     = models.CharField(max_length=30)
    status        = models.BooleanField(default=True)
    created_date  = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        managed = True
        db_table = "city"
        verbose_name_plural = "City Info"
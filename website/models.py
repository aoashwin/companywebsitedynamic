from django.db import models
from django.contrib import admin

# Create your models here.
class Product(models.Model):
    itemname = models.CharField(max_length=100)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='photos/')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('itemname', 'price', 'photo')

class People(models.Model):
    membername = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/')

class PeopleAdmin(admin.ModelAdmin) :
    list_display = ('membername', 'designation', 'photo')
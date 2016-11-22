from django.db import models

# Create your models here.


class UserInfo(models.Model):
    user = models.CharField(max_length=32)
    passwd = models.CharField(max_length=32)
    def __str__(self):
        return self.user



class product(models.Model):
    name = models.CharField(max_length=32)
    money = models.CharField(max_length=32)


    def __str__(self):
        return self.name


class shopping_cart(models.Model):
    user_name = models.CharField(max_length=32)
    nember = models.CharField(max_length=32)
    product_name = models.CharField(max_length=32)
    money = models.CharField(max_length=32,default=1)
    def __str__(self):
        return self.user_name

from django.contrib import admin

# Register your models here.

from mall import models

admin.site.register(models.UserInfo)
admin.site.register(models.product)
admin.site.register(models.shopping_cart)

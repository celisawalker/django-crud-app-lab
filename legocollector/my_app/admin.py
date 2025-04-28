from django.contrib import admin
from .models import Lego, Wishlist

# Register your models here.
admin.site.register([Lego, Wishlist])
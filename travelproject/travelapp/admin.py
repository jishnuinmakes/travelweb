from django.contrib import admin

# Register your models here.
from .models import Place, DP

admin.site.register(Place)
admin.site.register(DP)

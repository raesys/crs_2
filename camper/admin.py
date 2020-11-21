from django.contrib import admin
from .models import DifferentClasses, District, Camper


admin.site.register(DifferentClasses)
admin.site.register(District)
admin.site.register(Camper)
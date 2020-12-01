from django.contrib import admin
from .models import District, Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','local_church', 'district', 'balance', 'phone')
    list_filter = ('district',)


admin.site.register(District)
admin.site.register(Profile, ProfileAdmin)

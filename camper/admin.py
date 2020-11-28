from django.contrib import admin
from .models import DifferentClasses, Camper
from datetime import date

# For custom admin
from django.contrib.auth.models import User
from accounts.models import Profile
from django.urls import path
from django.db import models
from django.shortcuts import render


admin.site.site_header = "G.A. East Youth Camp 2020"
admin.site.site_title = "G.A. East Youth Camp 2020 Admin Area"
admin.site.index_title = "Welcome to the G.A. East Youth Camp 2020 Admin Area"


class CamperAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'gender', 'email', 'phone', 'different_class', 'created_by', 'local_church', 'district', 'calculate_age')
    list_filter = ('gender',)
    search_fields = ['last_name', 'different_class']
    prepopulated_fields = {}

    def local_church(self, obj):
        return obj.created_by.profile.local_church
    local_church.short_description = 'CB_Loc_Church'

    def district(self, obj):
        return obj.created_by.profile.district
    district.short_description = 'CB_District'

    def calculate_age(self, obj):
        today = date.today()
        birth_date = obj.date_of_birth
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age
    calculate_age.short_description = "Age"


admin.site.register(DifferentClasses)
admin.site.register(Camper, CamperAdmin)



# my dummy model
class DummyModel(models.Model):

    class Meta:
        verbose_name_plural = 'Dummy Model'
        # app_label = 'main'

def my_custom_view(request):
    # return HttpResponse('Admin Custom View')
    campers = Camper.objects.all()
    users = User.objects.all()
    total_campers = len(campers)
    total_users = len(users)
    users_and_campers = {}
    for user in users:
        user_campers = user.campers.all()
        user_total_campers = len(user_campers)
        try:
            profile_district = user.profile.district
        except Profile.DoesNotExist:
            profile_district = 'Not set yet'
        # users_and_campers[user.username] = user_total_campers
        users_and_campers[user.username] = [user_total_campers]
        users_and_campers[user.username].append(profile_district)

    context = {
        'total_campers': total_campers,
        'total_users': total_users,
        'users_and_campers': users_and_campers,
    }
    return render(request, 'my_custom_view.html', context)

class DummyModelAdmin(admin.ModelAdmin):
    model = DummyModel

    def get_urls(self):
        view_name = '{}_{}_changelist'.format(
            self.model._meta.app_label, self.model._meta.model_name)
        return [
            path('my_admin_path/', my_custom_view, name=view_name),
        ]
        
admin.site.register(DummyModel, DummyModelAdmin)
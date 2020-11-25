from django.urls import path
from . import views


app_name = 'camper'


urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.camper_list, name='list'),
    path('new/', views.new_camper, name='new'),
    path('<int:id>/update/', views.update_camper, name='update'),
    path('<int:id>/delete/', views.delete_camper, name='delete'),
    path('dashboard/', views.dashboard, name='dashboard'),
]

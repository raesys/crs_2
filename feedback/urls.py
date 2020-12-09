from django.urls import path
from . import views


app_name = 'feedback'


urlpatterns = [
    path('', views.feedback_new, name='new'),
    path('success/', views.feedback_success, name='success'),
]

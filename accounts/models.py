from django.db import models
from django.contrib.auth.models import User


class District(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    local_church = models.CharField(max_length=200, help_text='The name of your assembly without "A/G" as suffix')
    balance = models.DecimalField(default=0, decimal_places=2, max_digits=100)

    class Meta:
        ordering = ['district']

    def __str__(self):
        return f"{self.user.username}: {self.local_church}"

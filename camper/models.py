from django.db import models
from django.contrib.auth.models import User


class DifferentClasses(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Different Classes'
        ordering = ['name']

    def __str__(self):
        return self.name



class Camper(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
    )
    date_of_birth = models.DateField(help_text='Format: YYYY-MM-DD')
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    different_class = models.ForeignKey(DifferentClasses, verbose_name="Different Classes", on_delete=models.SET_NULL, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='campers')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


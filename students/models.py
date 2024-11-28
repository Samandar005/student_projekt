from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()

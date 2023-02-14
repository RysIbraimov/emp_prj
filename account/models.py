from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=30)
    education = models.CharField(max_length=300)
    location = models.CharField(max_length=100)
    age = models.IntegerField()
    job = models.CharField(max_length=300)

    def __str__(self):
        return self.user.username


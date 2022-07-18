from django.db import models

# Create your models here.
class BigDataComponent(models.Model):
    category = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    access_point = models.CharField(max_length=100, default='http://...')

    def __str__(self):
        return self.name

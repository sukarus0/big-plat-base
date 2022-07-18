from django.db import models

# Create your models here.
class Resources(models.Model):
    cpu = models.CharField(max_length=10)
    memory = models.CharField(max_length=10)

    def __str__(self):
        return 'Resources'

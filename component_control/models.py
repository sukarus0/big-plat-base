from django.db import models

# Create your models here.
class ComponentStatus(models.Model):
    name = models.CharField(max_length=20)
    status = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name} ({self.status})'

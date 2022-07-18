from django.db import models

# Create your models here.
class Resources(models.Model):
    cpu = models.CharField(max_length=10)
    memory = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'Resources - ({self.cpu}, {self.memory})'

class ClusterInfo(models.Model):
    component_type = models.CharField(max_length=20)
    number_of_members = models.IntegerField()

    def __str__(self):
        return f'{component_type}.cluster of {number_of_members} members'

from django.db import models

# Create your models here.

class Members(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    birth = models.DateTimeField()
    email = models.CharField(max_length=50)

    def __str__(self):
        return f'[{self.pk}]{self.name}'
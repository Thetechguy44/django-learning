from django.db import models

# Create your models here.
class Tour(models.Model):
    # defining fields for country and other related fileds needed
    origin_country = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    course = models.CharField(max_length=64)
    age = models.IntegerField()
    phone = models.IntegerField()

    def __str__(self):
        return (f"ID:{self.id}: From {self.origin_country} in {self.state} studying {self.course} at {self.age} with the phone number {self.phone}")
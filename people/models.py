from django.db import models
from datetime import time

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=60)
    image = models.ImageField(null=True)

    class Meta:
        abstract = True

class Employee(Person):
    availability_start = models.TimeField(default=time(hour=9))
    availability_end = models.TimeField(default=time(hour=17))

class Testimonial(Person):
    testimonial = models.TextField(max_length=300)

class Appointment(models.Model):
    date = models.DateTimeField()

    _employee = models.ForeignKey(to=Employee, on_delete=models.CASCADE)
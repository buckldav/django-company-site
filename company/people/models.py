from django.db import models
from datetime import time

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=60)
    image = models.ImageField(blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Employee(Person):
    pass

class Testimonial(Person):
    testimonial = models.TextField(max_length=300)

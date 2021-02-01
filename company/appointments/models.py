from django.db import models
from ..people.models import Employee

class Appointment(models.Model):
    date = models.DateTimeField()

    _employee = models.ForeignKey(
        to=Employee, 
        on_delete=models.CASCADE
    )
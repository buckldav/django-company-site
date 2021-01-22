from django.contrib import admin
from .models import Appointment, Employee, Testimonial

# Register your models here.
admin.site.register(Appointment)
admin.site.register(Employee)
admin.site.register(Testimonial)
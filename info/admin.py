from django.contrib import admin
from .models import Contact, Student, Take_attendence
# Register your models here.

admin.site.register(Contact)
admin.site.register(Student)
admin.site.register(Take_attendence)
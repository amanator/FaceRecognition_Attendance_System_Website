from django.db import models
from django.db.models.fields import DateTimeCheckMixin
from django.utils.timezone import now
from django.contrib import admin
# Create your models here.

admin.site.site_header = "GEHU Attendence"
admin.site.site_title = "Welcome to GEHU Attendence"
admin.site.index_title = "Welcome to this portal"



class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.TextField(max_length=100)
    content = models.TextField()
    timeStamp=models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.name

class Student(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    gender = models.CharField(max_length=13)
    university_roll_no = models.CharField(max_length=13, unique=True)
    email = models.TextField(max_length=100)
    post = models.TextField()
    student_img = models.ImageField(null=True, blank=True, upload_to="images/")
    timeStamp=models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.name + " ("+ self.post + ")"

class Take_attendence(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, default="")
    status = models.CharField(max_length=10, default="")
    attendence_date = models.CharField(max_length=10, default="")
    section = models.CharField(max_length=2, default="")
    university_roll = models.CharField(max_length=10, default="")
    employe = models.ForeignKey(Student, on_delete=models.CASCADE)
    date= models.DateTimeField(default=now, editable=False)
    def __str__(self):
        return  self.name+ " ("+self.attendence_date+" - " + self.status+ ")"
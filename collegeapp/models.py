from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Course(models.Model):
    course_name=models.CharField(max_length=255,null=True)
    fee=models.IntegerField(null=True)

    def __str__(self):
        return self.course_name

class Student(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    student_name=models.CharField(max_length=255,null=True)
    student_address=models.CharField(max_length=255,null=True)
    student_age=models.IntegerField(null=True,blank=True)
    joining_date=models.DateField()


    def __str__(self):
        return self.student_name
class Teacher(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    address=models.CharField(max_length=255)
    age=models.IntegerField(null=True)
    contact=models.CharField(max_length=255)
    image=models.ImageField(blank=True,null=True,upload_to="image/")
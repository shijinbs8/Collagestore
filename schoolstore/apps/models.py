from django.db import models

# Create your models here.
class Course(models.Model):
    cname=models.CharField(max_length=100)

    def __str__(self):
        return self.cname

class SubCourse(models.Model):
    sname=models.CharField(max_length=100)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return self.sname

class MyData(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    DOB=models.CharField(max_length=200)
    Gender=models.CharField(max_length=100)
    Phone_Number= models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Department=models.CharField(max_length=100)
    Course=models.CharField(max_length=100)
    Purpose=models.CharField(max_length=100)

    def __str__(self):
        return self.First_Name



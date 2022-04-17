from django.db import models

# Create your models here.
class Student(models.Model):
# each class variable represents a database i.e. table field in the model
    Student_Name = models.CharField(max_length=200)
    School_name = models.CharField(max_length=30)
    SSC_Percentage = models.IntegerField()
    Describe_Hobbies = models.CharField(max_length=200)
    Achivements = models.CharField(max_length=200)
    
    def __str__(self):
        return self.Student_Name + " - " + self.School_name
     
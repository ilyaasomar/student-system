from django.db import models
# Create your models here.
class Student(models.Model):
    student_no = models.PositiveBigIntegerField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    field_of_study = models.CharField(max_length=255)
    gpa = models.FloatField()


    def __str__(self):
        return f'Studnet:{self.first_name} {self.last}'
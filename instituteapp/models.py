from django.db import models

# Create your models here.
class Courses(models.Model):
    courses_name= models.CharField(max_length=100)
    fee=models.IntegerField()
    duration=models.CharField(max_length=100)
    start_date=models.DateTimeField(max_length=100)
    trainer_name=models.CharField(max_length=100)
    trainer_exp=models.CharField(max_length=100)
    training_mode=models.CharField(max_length=100)


class StudentsInfo(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobile=models.BigIntegerField()
    course=models.CharField(max_length=100)
    location=models.CharField(max_length=100)

class CommentData(models.Model):
    comment=models.TextField(max_length=1000)
    date=models.DateTimeField()
    user_name =models.CharField(max_length=100)
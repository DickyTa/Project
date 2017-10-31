from datetime import datetime,date

from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=200)


class Student(models.Model):
    student_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    def getid(self):
        return self.student_id.user_id
    def w_amount(self):
        return Wallet.objects.get(user_id = self.student_id).money
    def gets(self):
        return Booked_session.objects.filter(student_id = self)
    def date(self):
        return datetime.today()
    def tmr(self):
        
        return datetime.today()


class Tutor(models.Model):
    tutor_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    rating = models.FloatField(max_length=5)
    subject_tag= models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    hourly_rate = models.FloatField(max_length=10)
    T_type = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    def getid(self):
        return self.tutor_id.user_id
    def w_amount(self):
        return Wallet.objects.get(user_id = self.tutor_id).money
    def gets(self):
        return Booked_session.objects.filter(tutor_id = self)
    def date(self):
        return datetime.today()

class Wallet(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    money = models.FloatField(max_length=100)

class Booked_session(models.Model):
    tutor_id = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    start_time = models.DateTimeField('Session start time')
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    def dateee(self):
        return self.start_time.weekday()
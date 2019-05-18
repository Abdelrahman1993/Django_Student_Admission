from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfileInfo(models.Model):
    GRADE = [
        ('one', 'one'),
        ('two', 'two'),
        ('three', 'three'),
        ('four', 'four'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    faculty = models.CharField(max_length=50)
    grade = models.CharField(max_length=5, choices=GRADE)

    def __str__(self):
        return self.user.username

class Subject(models.Model):
  name = models.CharField(max_length=50)
  hours = models.IntegerField(default = 0, blank = False)
  user = models.ManyToManyField(User, through='Membership')

  def __str__(self):
    return self.name


class Membership(models.Model):
    SEMESTER = (
        ('first', 'first'),
        ('second', 'second'),
    )
    semester = models.CharField(max_length=6, choices=SEMESTER)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)




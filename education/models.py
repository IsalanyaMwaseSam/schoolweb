from django.db import models
from education.choices import *





#Create your models here.
class Campus(models.Model):
  campus = models.CharField(max_length=50)
  
  def __str__(self):
    return self.campus


  class Meta:
    verbose_name = "Campus"
    verbose_name_plural = "Campus"

class Application(models.Model):
  first_name = models.CharField(null=True, max_length=40)
  other_names = models.CharField(null=True, max_length=50)
  studytime = models.CharField(max_length=20, choices=STUDYTIME_CHOICES, default=None)
  level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default=None)
  gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default=None)
  courses = models.BooleanField()
  Date_of_birth = models.CharField(null=True, max_length=15)
  email = models.EmailField(null=True)
  phone = models.CharField(null=True, max_length=20)
  residence = models.TextField(null=True)
  nationality = models.TextField(null=True)
  where = models.TextField(null=True)
  file1 = models.FileField(null=True, blank=True)
  file2 = models.FileField(null=True, blank=True)
  file3 = models.FileField(null=True, blank=True)
  other_contact = models.TextField(null=True)
    
  class Meta:
    verbose_name = "Applications"
    verbose_name_plural = "Applications"

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    users = models.ForeignKey(User)
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    phoneno = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

class Messages(models.Model):
    employee = models.ForeignKey(Employee)
    messages = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.messages

    class Meta:
        ordering = ["-date"]




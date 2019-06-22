from django.db import models
from .validators import email_is_valid, email_exists

class Departament(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

# Create your models here.


class Employee(models.Model):
    Departament.__unicode__ = lambda s: s.name
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, validators=[email_is_valid, email_exists])
    departament = models.ForeignKey(Departament, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

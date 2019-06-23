from django.db import models
from .validators import email_is_valid
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


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
    email = models.CharField(max_length=200, validators=[email_is_valid])
    departament = models.ForeignKey(Departament, on_delete=models.CASCADE)

    """
    Validate if email exists
    """

    def email_exists(self, exclude=None):
        employees_count = Employee.objects.filter(email=self.email).count()
        if employees_count > 0:
            raise ValidationError(_('%(value)s ready exists in database'), params={'value': self.email})

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def clean(self):
        self.email_exists()

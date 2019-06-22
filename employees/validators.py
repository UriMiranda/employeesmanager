from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import validate_email

from .models import Employee


def email_is_valid(value):
    if not validate_email(value):
        raise ValidationError(
            _('%(value)s is not a valid e-mail'), params={'value': value})


def email_exists(value):
    employees_count = Employee.objects.filter(email=value).count()
    if employees_count > 0:
        raise ValidationError(
            _('%(value)s ready exists in database'), params={'value': value})

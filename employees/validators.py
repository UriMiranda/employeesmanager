from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import validate_email


def email_is_valid(value):
    validate_email(value)

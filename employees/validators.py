from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import validate_email


def email_is_valid(value):
    if not validate_email(value):
        raise ValidationError(
            _('%(value)s is not a valid e-mail'), params={'value': value})


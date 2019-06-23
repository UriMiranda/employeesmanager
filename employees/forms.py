from django import forms
from .models import Departament, Employee
from .validators import email_is_valid
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def email_exists(email):
    employees_count = Employee.objects.filter(email=email).count()
    if employees_count > 0:
        raise ValidationError(_('%(value)s ready exists in database'), params={
                              'value': email})


class EmployeeForm(forms.Form):
    name = forms.TextInput()
    email = forms.EmailField(validators=[email_exists, email_is_valid])
    departament = forms.ModelChoiceField(
        queryset=Departament.objects.all(), to_field_name="name")

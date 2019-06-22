from django import forms
from .models import Departament, Employee
from .validators import email_is_valid,email_exists

class EmployeeForm(forms.Form):
    name = forms.TextInput()
    email = forms.EmailField(validators=[email_is_valid, email_exists])
    departament = forms.ModelChoiceField(queryset=Departament.objects.all(), to_field_name="name")
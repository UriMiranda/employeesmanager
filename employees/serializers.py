from .models import Employee

from rest_framework import serializers

"""
    Employee serializer class
"""
class EmployeeSerializer(serializers.ModelSerializer):
    """
        Departament relationship
    """
    departament = serializers.StringRelatedField(many=False)

    class Meta:
        model = Employee
        fields = ('name', 'email', 'departament')

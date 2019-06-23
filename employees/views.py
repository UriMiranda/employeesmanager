from django.shortcuts import render
from .models import Employee
from rest_framework import viewsets
from .serializers import EmployeeSerializer
from django.http import JsonResponse, HttpResponseNotAllowed,HttpResponseServerError
import json
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


class EmployeeList(viewsets.ModelViewSet):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


@csrf_exempt
def add_employees(request):
    if request.method == "GET":
        return HttpResponseNotAllowed(['GET'])
    json_employee = json.loads(request.body.decode("utf-8"))
    try:
        employee = Employee()
        employee.name = json_employee['name']
        employee.email = json_employee['email']
        employee.departament_id = json_employee['departament']
        employee.save()
    except KeyError:
        return HttpResponseServerError('Malformed JSON')

    return JsonResponse({'status': 'success', 'message': 'Employee saved'})


def remove_employees(request, user_id):
    Employee.objects.filter(pk=user_id).delete()
    return JsonResponse({'status': 'success', 'message': 'Employee deleted'})

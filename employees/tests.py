import unittest
from django.test import TestCase, Client
from .models import Employee, Departament
import datetime
from django.core.exceptions import ValidationError
import json

class EmployeeTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.departament = Departament.objects.create(name='T.I')

    def test_employee_existing_validation(self):
        try:
            Employee.objects.create(
                name='Valid', email='validate@gmail.com', departament=self.departament)
            Employee.objects.create(
                name='Valid', email='validate@gmail.com', departament=self.departament)
            self.assertFalse(False)
        except (ValidationError):
            self.assertTrue(True)

    def test_employee_create_api(self):
        datetime_hash = datetime.datetime.now().strftime('%d-%m-%Y-%H-%M-%S')
        response = self.client.post('/employees/store', {
            'name': 'teste-'+datetime_hash,
            'email': 'test-'+datetime_hash+'@gmail.com',
            'departament': '1'
        }, content_type="application/json", format="json")
        self.assertEqual(response.status_code, 200)

    def test_employee_list_api(self):
        response = self.client.get(
            '/employees', HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 301)

    def test_departament_delete_api(self):
        response = self.client.get('/employees/delete/2',HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 301)

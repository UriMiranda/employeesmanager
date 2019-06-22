import unittest
from django.test import TestCase, Client
from .models import Employee, Departament
import datetime

# Create your tests here.


class EmployeeTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_employee_list(self):
        response = self.client.get('/employees')
        self.assertEqual(response.status_code, 200)

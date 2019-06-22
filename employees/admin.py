from django.contrib import admin
from .models import Departament, Employee

# Register your models here.

class DepartamentAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['name']

class EmployeeAdmin(admin.ModelAdmin):
    fields = ['name', 'email', 'departament']
    list_display = ['name', 'email', 'departament' ]

    @staticmethod
    def departament__name(self, employee):
        return employee.departament.name
    


admin.site.register(Departament, DepartamentAdmin)
admin.site.register(Employee, EmployeeAdmin)
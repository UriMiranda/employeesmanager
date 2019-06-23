from django.urls import path, include
from django.http import HttpResponse
from . import views
from rest_framework import routers

app_name = 'employees'

router = routers.DefaultRouter()
router.register('', views.EmployeeList)


urlpatterns = [
    path('', include(router.urls)),
    path('store', views.add_employees, name='store'),
    path('delete/<int:user_id>/', views.remove_employees, name='delete')
]
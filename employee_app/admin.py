from django.contrib import admin

from employee_app.models import Role, department, Employee

# Register your models here.
admin.site.register(department)
admin.site.register(Role)
admin.site.register(Employee)
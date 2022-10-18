from datetime import datetime
from django.shortcuts import render, HttpResponse
from .models import department, Role, Employee
from django.contrib import messages
from django.db.models import Q 

# Create your views here.
def index(request):
    return render(request, 'index.html')

def view_all(request):
    emps = Employee.objects.all()
    context = {
        'emps':emps
    }

    return render(request, 'view_all.html', context)

def add(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept = int(request.POST['dept'])
        salary = int(request.POST['salary'])
        phone = int(request.POST['phone'])
        role = int(request.POST['role'])
        bonous = int(request.POST['bonous'])

        new_emp = Employee(first_name=first_name, last_name=last_name, dept_id=dept, salary=salary,
                             role_id=role, bonous=bonous, hire_date = datetime.now(), phone=phone)
        new_emp.save()
        messages.success(request, "Employee added successfully")
        return render(request, 'add.html')

    elif request.method=='GET':
        return render(request, 'add.html')
    
    else:
        return HttpResponse("An error occured while adding employee")

def remove(request, emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            messages.success(request,"Employee removed successfully")
            return render(request, 'remove.html')

        except:
            return HttpResponse("Please enter a valid employee id")

    emps = Employee.objects.all()
    context={
        'emps':emps
    }
    return render(request, 'remove.html', context)

def filter(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']

        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name=dept)
        if role:
            emps = emps.filter(role__name=role)
        
        context={
            'emps':emps
        }

        return render(request, 'view_all.html', context)

    elif request.method=='GET':
        return render(request, 'filter.html')
    
    else:
        return HttpResponse("An error occured")
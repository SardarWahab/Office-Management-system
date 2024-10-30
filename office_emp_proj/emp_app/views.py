from django.shortcuts import render,redirect,HttpResponse
from .models import *
from datetime import datetime
# Create your views here.

def index(request):
 
    return render(request, 'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'view_all_emp.html',context)



def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        dept_id = request.POST.get('dept')  # Assuming this is the department ID
        salary = request.POST.get('salary')
        bonus = request.POST.get('bonus')
        role_id = request.POST.get('role')  # Assuming this is the role ID
        phone = request.POST.get('phone')
        hire_date = request.POST.get('hire_date')
        
        try:
            # Retrieve the Department instance
            department_instance = Department.objects.get(id=dept_id)
        except Department.DoesNotExist:
            return HttpResponse('Department not found', status=404)

        try:
            # Retrieve the Role instance
            role_instance = Role.objects.get(id=role_id)
        except Role.DoesNotExist:
            return HttpResponse('Role not found', status=404)

        new_emp = Employee(
            first_name=first_name,
            last_name=last_name,
            dept=department_instance,  # Pass the Department instance
            salary=salary,
            bonus=bonus,
            role=role_instance,  # Pass the Role instance
            phone=phone,
            hire_date=hire_date
        )
        new_emp.save()
        return HttpResponse('Data saved successfully...')
    
    elif request.method == 'GET':
        return render(request, 'add_emp.html')
    
    else:
        return render(request, 'add_emp.html')
def remove_emp(request):
    return render(request, 'remove_emp.html')

def filter_emp(request):
    return render(request, 'filter_emp.html')
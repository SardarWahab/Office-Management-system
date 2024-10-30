from django.shortcuts import render, redirect, HttpResponse
from .models import Department, Role, Employee
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'view_all_emp.html', context)

def add_emp(request):
    if request.method == 'POST':
        department = request.POST.get('department')
        role = request.POST.get('role')

        if department and role:
            dep = Department.objects.create(name=department)
            rol = Role.objects.create(name=role)
            messages.success(request,'Department and Role addded successfully...')
            return redirect(add_emp)

        # Adding an Employee
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        dept = request.POST.get('dept')  # Assuming this is the department ID
        salary = request.POST.get('salary')
        bonus = request.POST.get('bonus')
        role = request.POST.get('role')  # Assuming this is the role ID
        phone = request.POST.get('phone')
        hire_date = request.POST.get('hire_date')

        try:
            # Retrieve the Department instance
            department_instance = Department.objects.get(id=dept)
            role_instance = Role.objects.get(id=role)

            # Create new employee
            new_emp = Employee(
                first_name=first_name,
                last_name=last_name,
                dept=department_instance,
                salary=salary,
                bonus=bonus,
                role=role_instance,
                phone=phone,
                hire_date=hire_date
            )
            new_emp.save()
            messages.success(request,'Employee added successfully...')
            return redirect(all_emp)
        except Department.DoesNotExist:
            messages.error(request,'Department does not exist...')
            return redirect(add_emp)
        except Role.DoesNotExist:
            messages.error(request,'Role does not exist...')
            return redirect(add_emp)

    # Prepare context data for the form if not POST
    departments = Department.objects.all()
    roles = Role.objects.all()
    context = {
        'departments': departments,
        'roles': roles,
    }
    return render(request, 'add_emp.html', context)  # Render form with context data

def remove_emp(request, emp_id=None):
    if emp_id:
        emp = Employee.objects.filter(id=emp_id).first()  # Filter for a single employee, returns None if not found
        if emp:
            emp.delete()
            messages.success(request, 'Employee removed successfully.')
        else:
            messages.error(request, 'Employee does not exist.')
          
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'remove_emp.html', context)

def filter_emp(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dept = request.POST.get('dept')
        role = request.POST.get('role')
    return render(request, 'filter_emp.html')

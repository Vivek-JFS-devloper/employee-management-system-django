from django.shortcuts import render, redirect
from .models import Emp
import datetime

def emp_home(request):
    emps = Emp.objects.all()
    return render(request,'emp/index.html',{'emps':emps})

def emp_add(request):
    if request.method == 'POST':
        # Fetch data from form
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')  # lowercase
        department = request.POST.get('department')
        designation = request.POST.get('designation')
        salary = request.POST.get('salary')
        gender = request.POST.get('gender')
        address = request.POST.get('address')

        date_of_joining = datetime.datetime.now().date()

        # Create new employee
        emp = Emp(
            name=name,
            email=email,
            phone=phone,
            department=department,
            designation=designation,
            salary=salary,
            gender=gender,
            address=address,
            date_of_joining=date_of_joining
        )

        # Save object (employee_id will auto-generate from save() method)
        emp.save()

        print("Employee data saved successfully!")
        return redirect('/emp/home')

    return render(request, 'emp/add-emp.html')

def emp_delete(request,id):
    emp = Emp.objects.get(id = id)
    emp.delete()
    return redirect('/emp/home')

def emp_update(request,id):
    emp = Emp.objects.get(id = id)
    if request.method == 'POST':
      emp.name = request.POST.get('name')
      emp.email = request.POST.get('email')
      emp.phone = request.POST.get('phone')
      emp.department = request.POST.get('department')
      emp.designation = request.POST.get('designation')
      emp.salary = request.POST.get('salary')
      emp.gender = request.POST.get('gender')
      emp.address = request.POST.get('address')
      emp.save()
      return redirect("/emp/home")
    return render(request,'emp/update-emp.html',{"emp":emp})

def emp_contact(request):
    return render(request,'emp/contact-emp.html')


def emp_service(request):
    return render(request,'emp/service-emp.html')

def emp_about(request):
    return render(request,'emp/about-emp.html')
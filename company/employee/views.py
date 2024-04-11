from django.shortcuts import render, redirect
from employee.forms import EmployeeForm
from employee.models import Employee

# Create your views here.
def index(request):
    employees = Employee.objects.all()
    return render(request, "show.html", {'employees': employees})

def addnew(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = EmployeeForm()
    return render(request, "index.html", {'form': form})


def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, "edit.html", {'employee': employee})

def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/")  
    return render(request, 'edit.html', {'employee': employee})

def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/")
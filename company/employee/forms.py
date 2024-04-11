from django import forms
from employee.models import Employee
class EmployeeForm(forms.ModelForm):
    class Meta: 
        model = Employee
        fields = ['name', 'email', 'department', 'position', 'hire_date']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control'}),
                   'department': forms.TextInput(attrs={'class': 'form-control'}),
                   'position': forms.TextInput(attrs={'class': 'form-control'}),
                   'hire_date': forms.DateInput(attrs={'class': 'form-control'}),
                   }
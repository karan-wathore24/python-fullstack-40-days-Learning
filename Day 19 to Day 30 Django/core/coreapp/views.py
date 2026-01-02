from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request, 'contact.html')

from django.http import HttpResponse
from .models import Student

def add_student(request):
    Student.objects.create(
        name="Rahul",
        email="rahul@gmail.com",
        age=22
    )
    return HttpResponse("Student Added Successfully")

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})
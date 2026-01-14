from django.shortcuts import render , redirect ,  get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required


from django.http import HttpResponse
from .models import Student

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request, 'contact.html')


def add_student(request):
    return HttpResponse("Student Added Successfully")

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})
from django.http import HttpResponse

# def student_list(request):
#     # return render(request,"student.html")
#     return HttpResponse("STUDENT LIST VIEW WORKING")


def add_student(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')

        Student.objects.create(
            name=name,
            email=email,
            age=age
        )
        return redirect('student_list')

    return render(request, 'add_student.html')



def update_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.name = request.POST.get('name')
        student.email = request.POST.get('email')
        student.age = request.POST.get('age')
        student.save()
        return redirect('student_list')

    return render(request, 'update_student.html', {'student': student})


def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('student_list')


def user_login(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('student_list')
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('login')


# @login_required
# def student_list(request):
#     students = Student.objects.all()
#     return render(request, 'students.html', {'students': students})


# @permission_required('coreapp.view_student')
# def student_list(request):
#     students = Student.objects.all()
#     return render(request, 'students.html', {'students': students})

def test(request):
    return HttpResponse("OK WORKING")

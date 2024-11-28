from django.shortcuts import render
from .models import Student

def student_list(request):
    first_name = request.GET.get('first_name')
    last_name = request.GET.get('last_name')
    email = request.GET.get('email')
    age = request.GET.get('age')
    if first_name is not None and last_name is not None and email is not None and age is not None:
        Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            age=age
        )
    student = Student.objects.all()
    ctx = {'students': student}
    return render(request, 'students/student-list.html', ctx)
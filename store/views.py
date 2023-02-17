from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse, HttpResponseRedirect
from .models import Department, Course, Form


# Create your views here.
def index(request):
    department = Department.objects.all()
    return render(request, "home.html", {'department': department})


def register(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']
        c_password = request.POST['c_password']
        if password == c_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'User name taken')
                return render(request, 'register.html')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                print("user Created")
                return redirect('login')
        else:
            messages.info(request, 'Password not match')
            return render(request, 'register.html')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')


def form(request):
    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        phone = request.POST['phone']
        mail = request.POST['mail']
        address = request.POST['address']
        department = request.POST['department']
        course = request.POST['course']
        purpose = request.POST['purpose']
        materials_provide = request.POST.getlist('checks[]')
        form = Form(name=name, dob=dob, age=age, gender=gender, phone_number=phone, mail_id=mail,
                    address=address, department_id=department, course_id=course, purpose=purpose,
                    materials_provide=materials_provide)
        form.save()
        return render(request, 'success.html')
    else:
        department = Department.objects.all()
        # course = Course.objects.all()
        return render(request, "form.html", {'departments': department})


def get_course_ajax(request):
    if request.method == "POST":
        department_id = request.POST['department_id']
        try:
            department = Department.objects.filter(id=department_id).first()
            course = Course.objects.filter(department_id=department)
        except Exception:
            data['error_message'] = 'error'
            return JsonResponse(data)
        return JsonResponse(list(course.values('id', 'name')), safe=False)

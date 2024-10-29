from django.shortcuts import render,redirect,get_object_or_404
from collegeapp.models import Course,Student,Teacher
from django.contrib import messages
from django.urls import reverse 
from django.contrib.auth import authenticate,login,logout
import os
from django.contrib.auth.models import User,auth

def home(request):
    return render(request,'home.html')
def home1(request):
    teacher = Teacher.objects.get(user=request.user) 
    return render(request, 'th_home.html', {'teacher': teacher})
    

def adminpanel(request):
    return render(request,'admin.html')


def loginpage(request):
    if request.method == "POST":
        username=request.POST['uname']
        password=request.POST['pwd']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('adminpanel')   
            else:
                auth.login(request,user)
                messages.info(request,f'welcome  {username}')
                return redirect('home1')

        else:
            messages.info(request,"Invalid username or password")
            return redirect('/')
        return render(request,'home.html')
 


def add_course(request):
    return render(request,'add_course.html')

def add_course1(request):
    if request.method == 'POST':
        course_name=request.POST['Course']
        fee=request.POST['fee']
        course=Course(course_name=course_name,fee=fee)
        course.save()
        messages.success(request, f"{course.course_name} Added successfully")
        return redirect('add_course')

def add_student(request):
    course=Course.objects.all()
    return render(request,'add_student.html',{"courses":course})



def add_studentdb(request):
    if request.method == 'POST':
        student_name=request.POST['name']
        student_address=request.POST['address']
        student_age=request.POST['age']
        jdate=request.POST['jdate']
        sel=request.POST['sel']
        course1=Course.objects.get(id=sel)
        student=Student(student_name=student_name,student_address=student_address,student_age=student_age,joining_date=jdate,course=course1)
        student.save()
        messages.success(request, f"{student.student_name}'s details added successfully!")
        return redirect("show_student")
def show_student(request):
    student=Student.objects.all()
    return render(request,'show_student.html',{"students":student})

def deletepage(request,pk):
    student=Student.objects.get(id=pk)
    student.delete()
    return redirect('show_student')

def edit(request,pk):
    student=Student.objects.get(id=pk)
    cs=Course.objects.all()
    return render(request,'edit.html',{"students":student,"courses":cs})
def edit_db(request,pk):
    if request.method == 'POST':
        student=Student.objects.get(id=pk)
        cs=Course.objects.all()
        student.student_name=request.POST['ename']
        student.student_address=request.POST['eaddress']
        student.student_age=request.POST['eage']
        student.jdate=request.POST['ejdate']
        sel=request.POST['sel']
        course_id=Course.objects.get(id=sel)
        student.course=course_id
        student.save()
        messages.success(request, f"{student.student_name}'s details updated successfully!")
        return redirect("show_student")

def add_teacher(request):
    teacher=Teacher.objects.all()
    course=Course.objects.all()
    return render(request,'add_teacher.html',{"teacher":teacher,"courses":course})
def add_teacherdb(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        uname = request.POST.get('uname')
        password = request.POST.get('pwd')
        cpassword = request.POST.get('cpwd')
        address = request.POST.get('address')
        age = request.POST.get('age')
        email = request.POST.get('email')
        contact = request.POST.get('num')
        sel = request.POST.get('sel')

        # Check if the password matches
        if password != cpassword:
            return render(request, 'add_teacher.html', {'error': 'Passwords do not match', 'courses': Course.objects.all()})

        # Create user
        try:
            user = User.objects.create_user(
                username=uname,
                first_name=fname,
                last_name=lname,
                email=email,
                password=password
            )
        except Exception as e:
            return render(request, 'add_teacher.html', {'error': str(e), 'courses': Course.objects.all()})

        # Get the selected course
        course = Course.objects.get(id=sel)

        # Handle file upload if any
        image = request.FILES.get('file')

        # Create the Teacher instance
        teacher = Teacher(
            user=user,
            course=course,
            address=address,
            age=age,
            contact=contact,
            image=image
        )
        teacher.save()
        messages.success(request, f"{teacher.user.username} details added successfully!")
        return redirect('home')
    
    return render(request, 'add_teacher.html', {'courses': Course.objects.all()})
    


def show_teacher(request):
    teacher=Teacher.objects.all()
    return render(request,'show_teacher.html',{"teachers":teacher})

def th_delete(request,pk):
    teacher=Teacher.objects.get(id=pk)
    if teacher.image and os.path.isfile(teacher.image.path):
        os.remove(teacher.image.path)
    user = teacher.user
    user.delete()
    teacher.delete()
    return redirect('show_teacher') 

def profile(request):
    current_user = request.user.id
    user1 = Teacher.objects.get(user_id=current_user)
    return render(request, 'profile.html', {'users': user1})

def edit_teacher(request, pk):
   
    teacher = get_object_or_404(Teacher, id=pk)

    user = teacher.user  

    
    courses = Course.objects.all()

    return render(request, 'edit1.html', {
        'teacher': teacher,
        'user': user,
        'courses': courses
    })
def edit1_db(request, pk):   
    teacher = get_object_or_404(Teacher, id=pk)
    courses = Course.objects.all()  
    if request.method == 'POST':  
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        username = request.POST.get('uname')
        address = request.POST.get('address')
        age = request.POST.get('age')
        email = request.POST.get('email')
        contact = request.POST.get('num')
        course_id = request.POST.get('sel')  
        image = request.FILES.get('image')  

        user = teacher.user
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email
        user.save()

        teacher.address = address
        teacher.age = age
        teacher.contact = contact
        teacher.course = Course.objects.get(id=course_id)

        if image: 
            teacher.image = image
        teacher.save()       
        messages.success(request, f"{teacher.user.username}'s details updated successfully!")
        return redirect(reverse('home1'))  
    return render(request, 'th_home.html', {
        'teacher': teacher,
        'courses': courses
    })

def logoutpage(request):
    auth.logout(request)
    return redirect('home')
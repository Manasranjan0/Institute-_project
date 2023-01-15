from django.shortcuts import render,redirect
from .models import Courses,StudentsInfo,CommentData
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import RegistratonForm
import datetime as dt
date1=dt.datetime.now()

# Create your views here.
@login_required(login_url='loginpage')
def homePage(request):
    return render(request, 'homePage.html')
    
@login_required(login_url='loginpage')
def contactPage(request):
    if request.method=='GET':
        return render(request,'contactPage.html')

    else:
        StudentsInfo(
        first_name=request.POST['fname'],
        last_name=request.POST['lname'],
        email=request.POST['email'],
        mobile=request.POST['mob'],
        course=request.POST['course'],
        location=request.POST['loc']
        ).save()
    return redirect(contactPage)
   
@login_required(login_url='loginpage')
def servicePage(request):
    courses=Courses.objects.all()
    return render(request,'servicePage.html',{'courses':courses})

@login_required(login_url='loginpage')
def feedbackPage(request):
    if request.method == 'GET':
        comment=CommentData.objects.all().order_by('-id')
        return render(request,'feedbackPage.html',{'abc':comment})
    else:
        CommentData(
            comment=request.POST['content'],
            user_name=request.user,
            date=date1
        ).save()
        comment=CommentData.objects.all().order_by('-id')
        return render(request,'feedbackPage.html',{'abc':comment})


@login_required(login_url='loginpage')
def gallaryPage(request):
    return render(request, 'gallaryPage.html')


def loginpage(request):
    if request.method == 'GET':
        return render(request,'loginpage.html')
    
    else:
        user = request.POST['username']
        pwd=request.POST['password']
        user=authenticate(request,username=user,password=pwd)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('Invailid User Name/Password')

def logoutpage(request):
    logout(request)
    return redirect(loginpage)

def registerpage(request):
    if request.method == 'GET':
        form=RegistratonForm()
        return render(request, 'registerpage.html',{'form':form})
    else:
        form=RegistratonForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(user.password)
            form.save()
            return redirect(loginpage)
        else:
            return HttpResponse('Invalid Details')
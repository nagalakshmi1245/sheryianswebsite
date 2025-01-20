from django.shortcuts import render,redirect,HttpResponse
from .models import courses,request,loginModel
from.forms import requestForm,SignInForm,loginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    data=courses.objects.all()
    return render(request,'Home.html',{'course':data})


def course(request):
    data=courses.objects.all()
    return render(request,'Course.html',{'course':data})

def liveCourse(request):
    return render(request,'LiveCourse.html')

def requestCall(request):
    if request.method=='POST':
        f=requestForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('myapp:home')
    return render(request,'RequestCall.html',{'form':requestForm()})

def signIn(request):
    s=SignInForm()
    if request.method=='POST':
        f1=SignInForm(request.POST)
        if f1.is_valid():
            f1.save()
            return redirect('myapp:signin')
    return render(request,'SignIn.html',{'form':s})

def mail(request):
    return render(request,'Mail.html')

@login_required
def registered(request):
    return render(request,'register.html')
    

def loginView(request):
    l=loginForm()
    if request.method=='POST':
        f=loginForm(request.POST)
        if f.is_valid():
            username=f.cleaned_data.get('username')
            password=f.cleaned_data.get('password')
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect('myapp:registered')
            else:
                return HttpResponse('Invalid details')
    return render(request,'login.html',{'form':l})

def logoutView(request):
    logout(request)
    return redirect('myapp:login')
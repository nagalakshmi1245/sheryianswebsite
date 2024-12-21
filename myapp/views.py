from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'Home.html')
def course(request):
    return render(request,'Course.html')
def bootCamp(request):
    return render(request,'BootCamp.html')
def requestCall(request):
    return render(request,'RequestCall.html')
def signIn(request):
    return render(request,'SignIn.html')
def mail(request):
    return render(request,'Mail.html')
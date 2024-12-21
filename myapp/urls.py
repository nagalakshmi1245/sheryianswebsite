from django.urls import path
from .views import *

app_name='myapp'

urlpatterns=[
    path('',home,name='home'),
    path('course/',course,name='course'),
    path('bootcamp/',bootCamp,name='bootcamp'),
    path('requestcall/',requestCall,name='requestcall'),
    path('signin/',signIn,name='signin'),
    path('mail/',mail,name='mail')
]
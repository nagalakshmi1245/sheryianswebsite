from django.urls import path
from .views import *

app_name='myapp'

urlpatterns=[
    path('',home,name='home'),
    path('course/',course,name='course'),
    path('livecourse/',liveCourse,name='livecourse'),
    path('requestcall/',requestCall,name='requestcall'),
    path('signin/',signIn,name='signin'),
    path('mail/',mail,name='mail'),
    path('login/',loginView,name='login'),
    path('logout/',logoutView,name='logout'),
    path('register/',registered,name='registered')
]
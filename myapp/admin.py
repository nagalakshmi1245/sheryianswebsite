from django.contrib import admin
from .models import courses,request
from .forms import requestForm
# Register your models here.

class courseAdmin(admin.ModelAdmin):
    list_display=['name','price','language']

admin.site.register(courses,courseAdmin)

class requestAdmin(admin.ModelAdmin):
    list_display=['name','phone','date','enquiry']

admin.site.register(request,requestAdmin)
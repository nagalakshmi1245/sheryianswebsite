from django import forms
from.models import request,loginModel
from django.contrib.auth.models import User


class requestForm(forms.ModelForm):
    class Meta:
        model=request
        fields='__all__'

class SignInForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email']
    def save(self):
        obj=super().save()
        obj.set_password(self.cleaned_data['password'])
        obj.save()
        return obj

class loginForm(forms.ModelForm):
    class Meta:
        model = loginModel
        fields = '__all__'

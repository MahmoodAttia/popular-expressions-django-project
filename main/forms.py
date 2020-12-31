from main.models import Post
from django import forms
from django.contrib.auth.models import User
from django.forms.models import ModelForm

class reg(forms.ModelForm):
    password1 = forms.CharField(label='رمز الدخول',min_length=8,widget=forms.PasswordInput())
    password2 = forms.CharField(label='اعد ادخاله',min_length=8,widget=forms.PasswordInput())
    username = forms.CharField(label='اسم المستخدم')
    email = forms.EmailField(label='البريد الالكترونى')
    class Meta:
        model = User
        fields = (
            'username','password1','password2','email',
        )

    def clean_username(self):
        cd = self.cleaned_data
        if User.objects.filter(username=cd['username']).exists():
            raise forms.ValidationError('User already exists')
        return cd['username']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Password doesnt match')
        return cd['password2']

class Addpost(ModelForm):
    class Meta:
        model = Post
        fields =['title','content']


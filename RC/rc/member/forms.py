from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', )

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('age', 'gender', 'type', 'status', )

class SignUpForm(UserCreationForm):
    age = forms.IntegerField()
    gender = forms.CharField()
    type = forms.CharField()
    status = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'age', 'gender', 'type', 'status')
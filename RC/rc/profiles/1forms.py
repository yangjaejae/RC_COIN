from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class ProfileForm(UserCreationForm):
    username = forms.CharField()
    image = forms.ImageField(required=False)
    password1 = forms.CharField()
    password2 = forms.CharField()
    email = forms.EmailField()
    gender = forms.CharField(max_length=1)
    birth_year = forms.CharField(max_length=4)
    birth_month = forms.CharField(max_length=2)
    birth_date = forms.CharField(max_length=2)
    type = forms.IntegerField(required=False)
    status = forms.CharField(max_length=10, required=False)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'image', 'email', 'gender', 'birth_year', 'birth_month', 'birth_date', 'type', 'status',)

    def save(self, commit=True):
        user = super(ProfileForm, self).save(commit=False)
        user.gender = self.cleaned_data["gender"]
        user.birth_year = self.cleaned_data["birth_year"]
        user.birth_month = self.cleaned_data["birth_month"]
        user.birth_date = self.cleaned_data["birth_date"]
        user.type = 2
        user.status = "allowed"
        if commit:
            user.save()
        return user

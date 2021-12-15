from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db.models import fields
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = '__all__'


class CustomUpdateUserForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'email', ]

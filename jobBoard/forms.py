# job_board_app/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class UserRegistrationForm(UserCreationForm):
    is_employer = forms.BooleanField(required=False)
    phone_number = forms.CharField(max_length=15, required=False)
    country = forms.CharField(max_length=50, required=False)
    linkedin_account = forms.URLField(required=False)
    profile_picture = forms.ImageField(required=False)
    description = forms.CharField(widget=forms.Textarea)
    education = forms.CharField(max_length=100, required=False)
    current_job = forms.CharField(max_length=100, required=False)
    previous_jobs_experience = forms.CharField(widget=forms.Textarea, required=False)
    skills = forms.ModelMultipleChoiceField(queryset=Skill.objects.all(), required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'is_employer',
                  'phone_number', 'country', 'linkedin_account', 'profile_picture', 'description', 'education',
                  'current_job', 'previous_jobs_experience', 'skills']


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user', 'is_employer', 'join_date', 'skills']

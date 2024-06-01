# job_board_app/views.py
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.urls import reverse


def index(request):
    return render(request, 'jobBoard/index.html')


def user_logout(request):
    logout(request)
    return redirect('index')


def register(request):
    skills = Skill.objects.all()
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST, request.FILES)
        if user_form.is_valid():
            user = user_form.save()

            user_profile = UserProfile.objects.create(
                user=user,
                is_employer=user_form.cleaned_data.get('is_employer'),
                phone_number=user_form.cleaned_data.get('phone_number'),
                country=user_form.cleaned_data.get('country'),
                linkedin_account=user_form.cleaned_data.get('linkedin_account'),
                profile_picture=user_form.cleaned_data.get('profile_picture'),
                description=user_form.cleaned_data.get('description'),
                education=user_form.cleaned_data.get('education'),
                current_job=user_form.cleaned_data.get('current_job'),
                previous_jobs_experience=user_form.cleaned_data.get('previous_jobs_experience')
            )

            # Add skills to the user profile if provided
            selected_skills = request.POST.getlist('skills')
            if selected_skills:
                user_profile.skills.set(selected_skills)

            login(request, user)
            return redirect('user_profile', username=user.username)  # replace 'index' with the name of your index page

    else:
        user_form = UserRegistrationForm()
    return render(request, 'jobBoard/register.html', {'form': user_form, 'skills': skills})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('user_profile', username=user.username)  # replace 'index' with the name of your index page
    else:
        form = UserLoginForm()
    return render(request, 'jobBoard/login.html', {'form': form})


def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    user_profile = get_object_or_404(UserProfile, user=user)
    user_skills = user_profile.skills.all()
    return render(request, 'jobBoard/user_profile.html', {'user_profile': user_profile, 'user_skills': user_skills})


def all_profiles(request):
    search_query = request.GET.get('search', '')

    # Query profiles based on the search query
    profiles = UserProfile.objects.filter(user__username__icontains=search_query)
    # profiles = UserProfile.objects.all()
    return render(request, 'jobBoard/all_profiles.html', {'profiles': profiles})


def edit_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect(reverse('user_profile', args=[request.user.username]))  # Redirect to the user profile page
    else:
        form = EditProfileForm(instance=user_profile)

    return render(request, 'jobBoard/edit_profile.html', {'form': form})

# job_board_app/models.py

from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_employer = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15, blank=True)
    country = models.CharField(max_length=50, blank=True)
    linkedin_account = models.URLField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    description = models.TextField()
    education = models.CharField(max_length=100, blank=True)
    current_job = models.CharField(max_length=100, blank=True)
    previous_jobs_experience = models.TextField(blank=True)
    skills = models.ManyToManyField('Skill', blank=True)
    join_date = models.DateTimeField(auto_now_add=True)


class Skill(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

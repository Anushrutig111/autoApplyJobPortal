from django.db import models

class UserProfile(models.Model):
    email = models.EmailField(unique=True)
    resume = models.FileField(upload_to='resumes/')
    preferences = models.JSONField(default=dict)

    def __str__(self):
        return self.email

class JobListing(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    source = models.CharField(max_length=100)  # e.g., Naukri, LinkedIn
    url = models.URLField()
    fit_score = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.title} at {self.company}"

class UserProfile(models.Model):
    email = models.EmailField(unique=True)
    resume = models.FileField(upload_to='resumes/')  # 👈 Handles file upload
    preferences = models.JSONField(default=dict)

    def __str__(self):
        return self.email
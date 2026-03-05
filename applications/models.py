from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    applicant_name = models.CharField(max_length=255)
    email = models.EmailField()
    resume_link = models.URLField(blank=True)
    cover_letter = models.TextField(blank=True)
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant_name} - {self.job.title}"
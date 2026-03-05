from django.contrib import admin
from .models import Job, Application

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'posted_at', 'updated_at')
    search_fields = ('title', 'company', 'location')

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('applicant_name', 'email', 'job', 'applied_at')
    search_fields = ('applicant_name', 'email', 'job__title')
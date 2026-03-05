from rest_framework import serializers
from .models import Job, Application

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['id', 'title', 'description', 'company', 'location', 'status', 'posted_at', 'updated_at']

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'job', 'applicant_name', 'email', 'resume_link', 'cover_letter', 'status', 'applied_at']
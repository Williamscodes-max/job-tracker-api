from rest_framework import serializers
from .models import Job, Application

class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
        # 


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'
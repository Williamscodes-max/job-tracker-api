from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def api_home(request):
    return JsonResponse({
        "API": "Job Application Tracker API",
        "status": "running",
        "endpoints": {
            "jobs_list_create": "/api/jobs/",
            "job_detail": "/api/jobs/<id>/",
            "applications_list_create": "/api/applications/",
            "application_detail": "/api/applications/<id>/"
        }
    })

urlpatterns = [
    path('', api_home),
    path('admin/', admin.site.urls),
    path('api/', include('applications.urls')),
]
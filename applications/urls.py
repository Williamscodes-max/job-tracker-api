from django.urls import path
from .views import JobListCreateView, JobDetailView, ApplicationListCreateView, ApplicationDetailView

urlpatterns = [
    path('jobs/', JobListCreateView.as_view()),
    path('jobs/<int:pk>/', JobDetailView.as_view()),

    path('applications/', ApplicationListCreateView.as_view()),
    path('applications/<int:pk>/', ApplicationDetailView.as_view()),
]
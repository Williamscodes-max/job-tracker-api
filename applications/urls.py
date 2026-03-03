from django.urls import path
from .views import JobApplicationListCreateView, JobApplicationRetrieveUpdateDestroyView

urlpatterns = [
    path('applications/', JobApplicationListCreateView.as_view(), name='application-list-create'),
    path('applications/<int:pk>/', JobApplicationRetrieveUpdateDestroyView.as_view(), name='application-detail'),
]
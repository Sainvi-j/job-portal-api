from django.contrib import admin
from django.urls import path
from django.http import HttpResponse  
from api.views import (
    create_company,
    post_job,
    list_jobs,
    apply,
    list_applicants
)

def welcome(request):
    return HttpResponse("""
    <h1 style="color: blue;">Welcome to Job Portal API!</h1>
    <p>Available endpoints:</p>
    <ul>
        <li><a href="/api/jobs/">/api/jobs/</a> - List all jobs</li>
        <li>/api/create-company/ - Create company (POST)</li>
        <li>/api/post-job/ - Post a job (POST)</li>
        <li>/api/apply/ - Apply for job (POST)</li>
        <li><a href="/admin/">/admin/</a> - Admin panel</li>
    </ul>
    """)

urlpatterns = [
    path('', welcome),  # This handles the root URL
    path('admin/', admin.site.urls),
    path('api/create-company/', create_company),
    path('api/post-job/', post_job),
    path('api/jobs/', list_jobs),
    path('api/apply/', apply),
    path('api/applicants/<int:job_id>/', list_applicants),
]
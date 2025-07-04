import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Company, JobPost, Applicant

@csrf_exempt
@require_http_methods(["POST"])
def create_company(request):
    try:
        data = json.loads(request.body)
        company = Company.objects.create(
            name=data['name'],
            location=data['location'],
            description=data['description']
        )
        return JsonResponse({
            'id': company.id,
            'name': company.name,
            'location': company.location,
            'description': company.description,
            'created_at': company.created_at
        }, status=201)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
@require_http_methods(["POST"])
def post_job(request):
    try:
        data = json.loads(request.body)
        company = Company.objects.get(id=data['company_id'])
        job = JobPost.objects.create(
            company=company,
            title=data['title'],
            description=data['description'],
            salary=data['salary'],
            location=data['location']
        )
        return JsonResponse({
            'id': job.id,
            'company': job.company.name,
            'title': job.title,
            'description': job.description,
            'salary': job.salary,
            'location': job.location,
            'created_at': job.created_at
        }, status=201)
    except Company.DoesNotExist:
        return JsonResponse({'error': 'Company not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

@require_http_methods(["GET"])
def list_jobs(request):
    jobs = JobPost.objects.select_related('company').all()
    job_list = []
    for job in jobs:
        job_list.append({
            'id': job.id,
            'company': job.company.name,
            'title': job.title,
            'description': job.description,
            'salary': job.salary,
            'location': job.location,
            'created_at': job.created_at
        })
    return JsonResponse({'jobs': job_list})

@csrf_exempt
@require_http_methods(["POST"])
def apply(request):
    try:
        data = json.loads(request.body)
        job = JobPost.objects.get(id=data['job_id'])
        applicant = Applicant.objects.create(
            name=data['name'],
            email=data['email'],
            resume_link=data['resume_link'],
            job=job
        )
        return JsonResponse({
            'id': applicant.id,
            'name': applicant.name,
            'email': applicant.email,
            'resume_link': applicant.resume_link,
            'job_id': applicant.job.id,
            'applied_at': applicant.applied_at
        }, status=201)
    except JobPost.DoesNotExist:
        return JsonResponse({'error': 'Job not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

@require_http_methods(["GET"])
def list_applicants(request, job_id):
    try:
        job = JobPost.objects.get(id=job_id)
        applicants = Applicant.objects.filter(job=job)
        applicant_list = []
        for applicant in applicants:
            applicant_list.append({
                'id': applicant.id,
                'name': applicant.name,
                'email': applicant.email,
                'resume_link': applicant.resume_link,
                'applied_at': applicant.applied_at
            })
        return JsonResponse({
            'job_id': job.id,
            'job_title': job.title,
            'applicants': applicant_list
        })
    except JobPost.DoesNotExist:
        return JsonResponse({'error': 'Job not found'}, status=404)
# Job Portal API

A Django-based job portal API (without DRF).

## Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/create-company/` | POST | Create a new company |
| `/api/post-job/` | POST | Post a new job |
| `/api/jobs/` | GET | List all jobs |
| `/api/apply/` | POST | Apply for a job |
| `/api/applicants/<job_id>/` | GET | List applicants for a job |

## Setup
1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/job-portal-api.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the server:
   ```bash
   python manage.py runserver
   ```

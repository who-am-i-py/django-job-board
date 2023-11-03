from django.shortcuts import render
from django.http import Http404
from .models import Job
from django.core.paginator import Paginator
# Create your views here.
def job_list(request):
    all_jobs = Job.objects.all()
    paginator = Paginator(all_jobs, 2) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'jobs': page_obj}
    return render(request, 'job/job/list.html',context)

def job_detail(request, id):
    try:
        job = Job.objects.get(id=id)
    except Job.DoesNotExist:
        raise Http404('Job not found')
    return render(request,'job/job/detail.html', {'job': job})
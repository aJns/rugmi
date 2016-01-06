from django.http import HttpResponse
from django.template import loader

from .models import Submission


def index(request):
    latest_submissions = Submission.objects.order_by('-pub_date')[:5]
    template = loader.get_template('images/index.html')
    context = {
        'latest_submissions': latest_submissions,
    }
    return HttpResponse(template.render(context, request))

def submit(request):
    return HttpResponse("Hello. You're at the images submit page.")

def detail(request, submission_id):
    return HttpResponse("You're looking at submission %s." % submission_id)

def comment(request, submission_id):
    return HttpResponse("This the comment submission page for submission %s." % submission_id)

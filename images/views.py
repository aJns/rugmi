from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello. You're at the images index.")

def submit(request):
    return HttpResponse("Hello. You're at the images submit page.")

def detail(request, submission_id):
    return HttpResponse("You're looking at submission %s." % submission_id)

def comment(request, submission_id):
    return HttpResponse("This the comment submission page for submission %s." % submission_id)

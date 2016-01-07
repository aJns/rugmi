from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Submission, Comment


def index(request):
    latest_submissions = Submission.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('images/index.html')
    context = { 'latest_submissions': latest_submissions }
    return render(request, 'images/index.html', context)

def submit(request):
    return HttpResponse("Hello. You're at the images submit page.")

def detail(request, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id)
    return render(request, 'images/detail.html', {'submission': submission})

def comment(request, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id)
    try:
        comment_text = request.POST['comment']
    except (KeyError):
        return render(request, 'images/detail.html', {'submission': submission})
    else:
        comment = Comment(submission=submission, comment_text=comment_text)
        comment.save()
        return HttpResponseRedirect(reverse('images:detail', args=(submission.id,)))

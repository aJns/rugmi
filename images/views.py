from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Submission, Comment
from .forms import CommentForm


def index(request):
    latest_submissions = Submission.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('images/index.html')
    context = { 'latest_submissions': latest_submissions }
    return render(request, 'images/index.html', context)

def submit(request):
    return HttpResponse("Hello. You're at the images submit page.")

def detail(request, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id)
    form = CommentForm()
    return render(request, 'images/detail.html', {'submission': submission, 'form': form})

def comment(request, submission_id):
    current_submission = get_object_or_404(Submission, pk=submission_id)
    try:
        form = CommentForm(request.POST)
    except (KeyError):
        return render(request, 'images/detail.html', {'submission': submission})
    else:
        if form.is_valid():
            comment = Comment(submission=current_submission, comment_text=form.cleaned_data['comment_text'])
            comment.save()
        return HttpResponseRedirect(reverse('images:detail', args=(submission_id,)))

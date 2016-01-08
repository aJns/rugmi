from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Submission, Comment
from .forms import SubmissionForm, CommentForm


def index(request):
    latest_submissions = Submission.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('images/index.html')
    context = { 'latest_submissions': latest_submissions }
    return render(request, 'images/index.html', context)

def submit(request):
    if request.method == 'POST':
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            submission = Submission(title=form.cleaned_data['title'],
                                    description=form.cleaned_data['description'],
                                    content=form.cleaned_data['image'])
            submission.save()
            return HttpResponseRedirect(reverse('images:detail', args=(submission.id,)))
        else:
            print("Form isn't valid")
    else:
        form = SubmissionForm()
    return render(request, 'images/submit.html', {'form': form})

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

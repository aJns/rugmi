from django import forms


class CommentForm(forms.Form):
    comment_text = forms.CharField(label='', max_length=500, widget=forms.Textarea)

class SubmissionForm(forms.Form):
    title = forms.CharField(label='Submission title', max_length=100)
    description = forms.CharField(label='Description', max_length=500, widget=forms.Textarea)
    image = forms.ImageField()

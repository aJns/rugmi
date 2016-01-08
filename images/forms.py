from django import forms


class CommentForm(forms.Form):
    comment_text = forms.CharField(label='Your comment', max_length=500)

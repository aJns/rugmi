from django.db import models


class Submission(models.Model):
    title = models.CharField(max_length=75)
    description = models.CharField(max_length=500)
    pub_date = models.DateTimeField(auto_now_add=True)
    content = models.ImageField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField(auto_now_add=True)

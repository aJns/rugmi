from django.conf.urls import url

from . import views

app_name = 'images'
urlpatterns = [
    # ex: /images/
    url(r'^$', views.index, name='index'),

    # ex: /images/5/
    url(r'^(?P<submission_id>[0-9]+)/$', views.detail, name='detail'),

    # ex: /images/5/comment
    url(r'^(?P<submission_id>[0-9]+)/comment/$', views.comment, name='comment'),

    # ex: /images/submit
    url(r'^submit/$', views.submit, name='submit'),
]

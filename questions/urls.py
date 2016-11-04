"""quiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from questions import views

urlpatterns = [
    url(r'^(?P<quiz_pk>\d+)/$', views.questions, name='questions'),
    url(r'^start/(?P<quiz_pk>\d+)/$', views.start, name='start'),
    url(r'^reset/(?P<quiz_pk>\d+)/$', views.reset, name='reset'),
    url(r'^make_right/(?P<answer_pk>\d+)/(?P<question_pk>\d+)/(?P<quiz_pk>\d+)/$', views.make_right, name='make_right'),
    url(r'^delete_answer/(?P<answer_pk>\d+)/(?P<quiz_pk>\d+)/$', views.delete_answer, name='delete_answer'),
    url(r'^delete_question/(?P<question_pk>\d+)/(?P<quiz_pk>\d+)/$', views.delete_question, name='delete_question'),
    url(r'^end_page/(?P<right>\d+)/(?P<total>\d+)/(?P<quiz_pk>\d+)/$', views.end_page, name='end_page'),

]

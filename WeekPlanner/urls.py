from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^edu_result/(?P<question_id>[0-9]+)/$', views.educational_activity_result,
        name='educational_activity_result')
]

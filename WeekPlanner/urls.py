from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^edu_result/(?P<activity_id>[0-9]+)/$', views.educational_activity_result_id,
        name='educational_activity_result'),
    url(r'^edu_result/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d+)/(?P<activity_id>[0-9]+)/$',
        views.educational_activity_result_create_activity_id, name='educational_activity_result'),
    url(r'^edu_result/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d+)/$',
        views.educational_activity_result_create, name='educational_activity_result')
]

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^edu_result/(?P<activity_id>[0-9]+)/$', views.educational_activity_result_id,
        name='educational_activity_result'),
    url(r'^edu_result/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d+)/(?P<activity_id>[0-9]+)/$',
        views.educational_activity_result_create_activity_id, name='educational_activity_result'),
    url(r'^edu_result/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d+)/$',
        views.educational_activity_result_create, name='educational_activity_result'),
    url(r'^phys_result/(?P<activity_id>[0-9]+)/$', views.physical_activity_result_id,
        name='physical_activity_result'),
    url(r'^phys_result/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d+)/(?P<activity_id>[0-9]+)/$',
        views.physical_activity_result_create_activity_id, name='physical_activity_result'),
    url(r'^phys_result/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d+)/$',
        views.physical_activity_result_create, name='physical_activity_result'),
    url(r'single_task/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d+)/$',
        views.single_task_create, name='single_task'),
    url(r'single_task/(?P<task_id>[0-9]+)/$',
        views.single_task_id, name='single_task')
]

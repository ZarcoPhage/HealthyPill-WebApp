from django.urls import path, re_path
from HealthyPillApp import views
from HealthyPillApp.views import *


urlpatterns = [
    path('perfil/', perfil),
    path('', views.base, name="base"),
    path('calendario/', views.CalendarView.as_view(), name='calendario'),
    re_path(r'^event/new/$', views.event, name='event_new'),
    re_path(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
]

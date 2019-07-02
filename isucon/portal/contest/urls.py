from django.contrib import admin
from django.urls import path, include

from isucon.portal.contest import views

app_name = 'contest'
urlpatterns = [
    path('', views.index, name="index"),
    path('dashboard/', views.dashboard, name="dashboard"),

    path('servers/', views.servers, name="servers"),
    path('teams/', views.teams, name="teams"),

    path('jobs/', views.jobs, name="jobs"),
    path('jobs/<int:pk>/', views.job_detail, name="job_detail"),
    path('scores/', views.scores, name="scores"),

    path('settings/server', views.settings_server, name="settings_server"),
    path('settings/team', views.settings_team, name="settings_team"),
    path('settings/user', views.settings_user, name="settings_user"),
]

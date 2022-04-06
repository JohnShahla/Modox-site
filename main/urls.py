from django.urls import path

from .views import (
    home_view,
    detail_view,
    project_list,
)


app_name='main'

urlpatterns = [
    path('', home_view, name='home'),
    path('projects/<slug:slug>/', detail_view, name='details'),
    path('project-list/', project_list, name='project-list'),
]
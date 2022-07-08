from django.urls import path

from .views import (
    home_view,
    detail_view,
    project_add,
)


app_name='main'

urlpatterns = [
    path('', home_view, name='home'),
    path('projects/<slug:slug>/', detail_view, name='details'),

    path('administrator/project/add/', project_add, name='project_add'),
]
from django.urls import path

from .views import (
    home_view,
    detail_view,
)


app_name='main'

urlpatterns = [
    path('', home_view, name='home'),
    path('projects/<slug:slug>/', detail_view, name='details'),
]
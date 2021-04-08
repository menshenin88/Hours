from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='accounts'),
    path('time_tracker', views.overview, name='time_tracker')
]

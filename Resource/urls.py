from django.urls import path
from .views import Home
from . import views
urlpatterns=[ 
    path('',views.Home.as_view(), name='home'),
    path('resources',views.resources_list, name='resources'),
    path('resources/upload',views.upload_resources, name='upload'),
]
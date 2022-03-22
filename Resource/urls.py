from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from . import views
urlpatterns=[ 
    path('',views.Home.as_view(), name='home'),
    path('resources/',views.resources_list, name='resources'),
    path('resources/',views.resources_list, name='resources'),
]
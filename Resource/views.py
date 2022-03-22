from django.shortcuts import render
from django.views.generic import TemplateView
def resources_list(request):
    return render(request,'resources_list.html')
def upload_resources(request):
    return render(request,'upload_resources.html')
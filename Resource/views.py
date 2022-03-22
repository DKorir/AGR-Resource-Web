from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import ResourceForm
class Home(TemplateView):
    template_name='home.html'
def resources_list(request):
    return render(request,'resources_list.html')
def upload_resources(request):
    return render(request,'upload_resources.html')
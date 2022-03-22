from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .forms import ResourceForm
class Home(TemplateView):
    template_name='home.html'
def resources_list(request):
    return render(request,'resources_list.html')
def upload_resources(request):
    if request.method == 'POST':
        form=ResourceForm()
        if form.is_valid():
            form.save()
            return redirect('resources_list')
    else:
        form=ResourceForm()
    return render(request,'upload_resources.html', {
        'form': form
    })
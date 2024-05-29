from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView, CreateView
from django.urls import reverse_lazy
from .models import Project
from .forms import ProjectForm

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, 'projects/home.html')
    else:
        return redirect('accounts:login')
    
class ProjectListView(ListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'

class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('projects:projects')

class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('projects:projects')

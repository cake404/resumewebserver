from django.shortcuts import render
from .models import Project
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'projectsapp/index.html'
    context_object_name = 'project_list'

    def get_queryset(self):
        return Project.objects.all()

class ProjectDetailView(generic.DetailView):
    model = Project
    template_name = 'projectsapp/project_detail.html'

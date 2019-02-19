from django.shortcuts import render
from .models import Project
from django.views import generic
from django.http import JsonResponse

import json


class IndexView(generic.ListView):
    template_name = 'resumeapp/index.html'
    context_object_name = 'project_list'

    def get_queryset(self):
        return Project.objects.all()

def get_project_details(request):
    id = request.GET.get('id', None)
    project = Project.objects.get(pk=id)
    project_json = {
        'id' : project.id,
        'title' : project.title,
        'description' : project.description, 
        'image_url' : project.image_url,
        'github_link' : project.github_link,
        'technologies' : [tech.attributes() for tech in project.technologies.all()]
    }
    return JsonResponse(project_json)

    
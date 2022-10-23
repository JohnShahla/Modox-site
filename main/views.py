from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Project
from .forms import ProjectCreationForm

from contact.forms import MessageForm

def home_view(request):
    projects = Project.objects.all()

    web = Project.objects.filter(categories__name = 'web').count()
    android = Project.objects.filter(categories__name = 'android').count()
    ai = Project.objects.filter(categories__name = 'ai').count()
    financial_ai = Project.objects.filter(categories__name = 'financial_ai').count()
    graphic = Project.objects.filter(categories__name = 'graphic').count()

    form = MessageForm(request.POST or None)

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            form = MessageForm()
            return redirect(reverse("main:home"))

    context = {    
        'projects': projects,
        'form': form,

        'web': web,
        'android': android,
        'ai': ai,
        'financial_ai': financial_ai,
        'graphic': graphic
    }

    return render(request, 'main/index.html', context)


def detail_view(request, slug):
    project = get_object_or_404(Project, slug=slug)

    if project:
        if not request.user.is_authenticated:
            project.views += 1
            project.save()

    context = {
        'project': project,
    }

    return render(request, 'main/project-details.html', context)


def project_add(request):

    if request.method == 'POST':
        form = ProjectCreationForm(request.POST)

        if form.is_valid():
            instance = form.save()

            return HttpResponseRedirect('/administrator/project/add/')
    
    else:
        form = ProjectCreationForm()

    context = {
        'form': form,
    }

    return render(request, 'main/add-project.html', context)


def error_404_view(request, *args, **kwargs):
    return render(request, '404.html')
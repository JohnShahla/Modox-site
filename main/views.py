from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Project, ProjectImages

from contact.forms import MessageForm

def home_view(request):
    projects = Project.objects.all()

    web = Project.objects.filter(categories__name = 'web').count()
    android = Project.objects.filter(categories__name = 'android').count()
    ai = Project.objects.filter(categories__name = 'ai').count()
    system = Project.objects.filter(categories__name = 'system').count()

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
        'system': system
    }

    return render(request, 'main/index.html', context)


def detail_view(request, slug):
    project = get_object_or_404(Project, slug=slug)

    images = ProjectImages.objects.filter(project=project)

    if project:
        if not request.user.is_authenticated:
            project.views += 1
            project.save()

    context = {
        'project': project,
        'images': images,
    }

    return render(request, 'main/project-details.html', context)


def error_404_view(request, *args, **kwargs):
    return render(request, '404.html')
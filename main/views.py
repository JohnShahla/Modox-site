from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Project, CV

from contact.forms import MessageForm
from skills.models import Skill

def home_view(request):
    projects = Project.objects.all()
    cv = CV.objects.all().first()

    frontend = Skill.objects.filter(tag__name='frontend')
    backend = Skill.objects.filter(tag__name='backend')
    other = Skill.objects.filter(tag__name='other')

    form = MessageForm(request.POST or None)

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            form = MessageForm()
            return redirect(reverse("main:home"))

    context = {
        'frontend': frontend,
        'backend': backend,
        'other': other,
        
        'projects': projects,
        'cv': cv,
        'form': form,
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


def project_list(request):
    projects_list = Project.objects.all()

    paginator = Paginator(projects_list, 9)
    page = request.GET.get('page')

    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)


    context = {
        'projects': projects,
    }

    return render(request, 'main/project-list.html', context)


def error_404_view(request, *args, **kwargs):
    return render(request, '404.html')
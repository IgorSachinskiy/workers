from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect

from project.slaves.forms import ResumeForms
from project.slaves.models import Resume


def index_view(request):
    """Вью отображает главную страницу приложения"""
    context = {
            'queryset': None,
            }
    return render(request, 'forum/index.html', context)

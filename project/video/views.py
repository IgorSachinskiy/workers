from django.shortcuts import render

from . import models

def index_view(request):
    """Вью отображает главную страницу приложения"""
    qs = models.Video.objects.all()
    context = {
            'queryset': qs,
            }
    return render(request, 'video/index.html', context)
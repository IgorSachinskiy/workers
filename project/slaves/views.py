from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect

from project.slaves.forms import ResumeForms
from project.slaves.models import Resume


def index_view(request):
    """Вью отображает главную страницу приложения"""
    qs = Resume.objects.all()
    context = {
            'title': 'Поиск работы',
            'queryset': qs,
            }
    return render(request, 'slaves/index.html', context)

def create_view(request):
    """Показывает или обрабатывает форму"""
    form = ResumeForms(request.POST or None)
    context = {
        'form': form,
        }
    if request.method == 'POST' and form.is_valid():
        if request.user.is_anonymous:
            return HttpResponseForbidden('Не авторизован')
        form.save(request.user)
        return redirect('slaves:index')
    return render(request, 'slaves/create.html', context)
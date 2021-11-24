from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.generic import FormView, TemplateView
from project.accounts import forms


class RegisterView(FormView):
    template_name = 'registration/register_form.html'
    form_class = forms.RegisterForm
    success_url = reverse_lazy('accounts:register_done')

    @method_decorator(csrf_protect)
    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = self.get_form()
            if form.is_valid():
                form.save()
        return super().dispatch(request, *args, **kwargs)


class RegisterDoneView(TemplateView):
    template_name = 'registration/register_done.html'
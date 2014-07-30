from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django_core.views.mixins.auth import LoginRequiredViewMixin
from umanage.change_password.forms import UManagePasswordChangeForm


class ChangePasswordView(LoginRequiredViewMixin, FormView):
    """View for changing a user's password."""

    template_name = 'umanage/change_password/change_password.html'
    form_class = UManagePasswordChangeForm

    def get_form_kwargs(self):
        form_kwargs = super(ChangePasswordView, self).get_form_kwargs()
        form_kwargs['user'] = self.request.user
        return form_kwargs

    def form_valid(self, form):
        form.save()
        return super(ChangePasswordView, self).form_valid(form)

    def get_success_url(self):
        return reverse('umanage_change_password_success')


class ChangePasswordSuccessView(LoginRequiredViewMixin, TemplateView):

    template_name = 'umanage/change_password/change_password_success.html'

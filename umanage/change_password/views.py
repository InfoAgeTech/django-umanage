from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.http.response import HttpResponseForbidden
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django_core.utils.urls import is_legit_next_url
from django_core.views.mixins.auth import LoginRequiredViewMixin

from ..forgot_password.forms import UManageSetPasswordForm
from .forms import UManagePasswordChangeForm


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
    """View for when a password has successfully been changed."""
    template_name = 'umanage/change_password/change_password_success.html'


class SetPasswordView(LoginRequiredViewMixin, FormView):
    """View for a user who has an unusable password and needs to set a
    password.  This can happen if a user authenticates through a 3rd party
    system and no usable password has been set.
    """
    template_name = 'umanage/change_password/set_password.html'
    form_class = UManageSetPasswordForm

    def get_form_kwargs(self):
        form_kwargs = super(SetPasswordView, self).get_form_kwargs()
        form_kwargs['user'] = self.request.user
        return form_kwargs

    def get_initial(self):
        initial = super(SetPasswordView, self).get_initial()
        initial['next'] = self.request.GET.get('next')
        return initial

    def post(self, request, *args, **kwargs):

        if request.user.has_usable_password():
            # this user already has a usable password and should not be posting
            # to this view.
            return HttpResponseForbidden()

        return super(SetPasswordView, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()

        next_url = form.cleaned_data.get('next')
        if is_legit_next_url(next_url=next_url):
            self.success_url = next_url

        return super(SetPasswordView, self).form_valid(form)

    def get_success_url(self):
        return self.success_url or reverse('umanage_change_password_success')

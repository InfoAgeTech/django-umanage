from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.views.generic.base import View
from django.views.generic.edit import FormView
from django_core.views.mixins.auth import LoginRequiredViewMixin

from ..mixins.views import AuthorizationTokenRequiredViewMixin
from ..models import ChangeEmailAuthorization
from .forms import ChangeEmailForm


class ChangeEmailView(LoginRequiredViewMixin, FormView):
    """View for changing a user's email."""

    template_name = 'umanage/change_email/change_email.html'
    form_class = ChangeEmailForm

    def get_form_kwargs(self):
        form_kwargs = super(ChangeEmailView, self).get_form_kwargs()
        form_kwargs['user'] = self.request.user
        return form_kwargs

    def form_valid(self, form):
        form.send_email()
        return super(ChangeEmailView, self).form_valid(form)

    def get_success_url(self):
        return reverse('umanage_change_email_sent')


class ChangeEmailSentView(LoginRequiredViewMixin, TemplateView):
    """View that confirms an email will be sent to the user to update the
    email address.
    """
    template_name = 'umanage/change_email/change_email_sent.html'


class ChangeEmailSuccessView(LoginRequiredViewMixin, TemplateView):
    """View that confirms an email has been updated successfully."""
    template_name = 'umanage/change_email/change_email_success.html'


class ChangeEmailActivationView(LoginRequiredViewMixin,
                                AuthorizationTokenRequiredViewMixin, View):

    authorization_class = ChangeEmailAuthorization

    def get(self, request, *args, **kwargs):

        # It's a valid change email object, update the user's email
        self.request.user.email = self.authorization.new_email_address
        self.request.user.save()

        # Expire the change email token so it's no longer valid.
        self.authorization.expire()
        return redirect('umanage_change_email_success')


class ChangeEmailExpiredView(LoginRequiredViewMixin, TemplateView):

    template_name = 'umanage/change_email/change_email_expired.html'

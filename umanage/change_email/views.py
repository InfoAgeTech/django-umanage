from __future__ import unicode_literals

from django.contrib import messages
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django_core.views.mixins.auth import LoginRequiredViewMixin
from umanage.change_email.forms import ChangeEmailForm


class ChangeEmailView(LoginRequiredViewMixin, FormView):
    """View for changing a user's email."""

    template_name = 'umanage/change_email/change_email.html'
    form_class = ChangeEmailForm

    def get_initial(self):
        initial = super(ChangeEmailView, self).get_initial()
        initial['current_email'] = self.request.user.email
        return initial

    def get_form_kwargs(self):
        form_kwargs = super(ChangeEmailView, self).get_form_kwargs()
        form_kwargs['user'] = self.request.user
        return form_kwargs

    def form_valid(self, form):
        # TODO: send emails to current and new email addresses notifying them
        #      of the change and providing the new email address a link to
        #      activate the new email address
        form.send_email()
        messages.success(self.request, _('Email sent with instructions on how '
                                         'to activate your new email address.'))
        return super(ChangeEmailView, self).form_valid(form)

    def get_success_url(self):
        return reverse('umanage_change_email')


class ChangeEmailActivationView(LoginRequiredViewMixin, TemplateView):

    template_name = 'umanage/change_email/change_email_activation.html'

    def get(self, request, *args, **kwargs):
        # TODO: get the ChangeEmail object by id to verify and save change.
        return super(ChangeEmailActivationView, self).get(request, *args,
                                                          **kwargs)

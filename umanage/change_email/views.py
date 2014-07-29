from __future__ import unicode_literals

from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.utils.translation import ugettext as _
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django_core.views.mixins.auth import LoginRequiredViewMixin
from umanage.change_email.forms import ChangeEmailForm
from umanage.models import ChangeEmail


class ChangeEmailView(LoginRequiredViewMixin, FormView):
    """View for changing a user's email."""

    template_name = 'umanage/change_email/change_email.html'
    form_class = ChangeEmailForm

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

    template_name = 'umanage/change_email/change_email_invalid.html'

    def get(self, request, *args, **kwargs):
        # TODO: get the ChangeEmail object by id to verify and save change.
        change_email = ChangeEmail.objects.get_by_token_or_404(
            token=kwargs.get('change_email_token'),
            created_user=self.request.user
        )

        if not change_email.is_valid():
            return super(ChangeEmailActivationView, self).get(request, *args,
                                                              **kwargs)

        # It's a valid change email object, update the user's email
        self.request.user.email = change_email.new_email_address
        self.request.user.save()

        # Expire the change email token so it's no longer valid.
        change_email.expire()

        msg = _('Email address confirmed and updated to {0}!'.format(
                                             change_email.new_email_address))
        messages.success(request, message=msg)
        return redirect('umanage_change_email')

from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.views.generic.edit import FormView
from django_core.views.mixins.auth import LoginRequiredViewMixin


class ChangePasswordView(LoginRequiredViewMixin, FormView):
    """View for changing a user's password."""

    template_name = 'umanage/change_password/change_password.html'
    form_class = PasswordChangeForm

    def get_form_kwargs(self):
        form_kwargs = super(ChangePasswordView, self).get_form_kwargs()
        form_kwargs['user'] = self.request.user
        return form_kwargs

    def form_valid(self, form):
        form.save()
        # update_session_auth_hash(self.request, form.user)
        messages.success(self.request, _('Successfully changed password!'))
        return super(ChangePasswordView, self).form_valid(form)

    def get_success_url(self):
        return reverse('umanage_change_password')

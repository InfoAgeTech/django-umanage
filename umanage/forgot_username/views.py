from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from .forms import ForgotUsernameForm
from django.shortcuts import redirect


class ForgotUsernameView(FormView):

    template_name = 'umanage/forgot_username/forgot_username.html'
    form_class = ForgotUsernameForm

    def get(self, request, *args, **kwargs):

        if request.user.is_authenticated():
            # User is authenticated, no need for this flow.
            return redirect('/')

        return super(ForgotUsernameView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        form.send_email()
        return super(ForgotUsernameView, self).form_valid(form)

    def get_success_url(self):
        return reverse('umanage_forgot_username_sent')


class ForgotUsernameSentView(TemplateView):

    template_name = 'umanage/forgot_username/forgot_username_sent.html'

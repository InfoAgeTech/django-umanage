from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.http.response import Http404
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from ..mixins.views import AuthorizationTokenRequiredViewMixin
from ..models import ForgotPasswordAuthorization
from .forms import ForgotPasswordForm
from .forms import UManageSetPasswordForm


class ForgotPasswordView(FormView):

    template_name = 'umanage/forgot_password/forgot_password.html'
    form_class = ForgotPasswordForm

    def get(self, request, *args, **kwargs):

        if request.user.is_authenticated():
            return redirect('/')

        return super(ForgotPasswordView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        form.send_email()
        return super(ForgotPasswordView, self).form_valid(form)

    def get_success_url(self):
        return reverse('umanage_forgot_password_sent')


class ForgotPasswordSentView(TemplateView):

    template_name = 'umanage/forgot_password/forgot_password_sent.html'


class ForgotPasswordChangePasswordView(AuthorizationTokenRequiredViewMixin,
                                       FormView):

    template_name = 'umanage/forgot_password/forgot_password_change_password.html'
    form_class = UManageSetPasswordForm
    authorization_class = ForgotPasswordAuthorization

    def get_authorization_user(self):
        if self.authorization_user is not None:
            return self.authorization_user

        User = get_user_model()

        try:
            user = User.objects.get(username=self.kwargs.get('username'))
        except User.DoesNotExist as e:
            raise Http404

        self.authorization_user = user
        return user

    def get_auth_expired_url(self):
        return reverse('umanage_forgot_password_expired')

    def get_form_kwargs(self):
        kwargs = super(ForgotPasswordChangePasswordView,
                       self).get_form_kwargs()
        kwargs['user'] = self.get_authorization_user()
        return kwargs

    def form_valid(self, form):
        form.save()
        self.authorization.expire()
        return super(ForgotPasswordChangePasswordView, self).form_valid(form)

    def get_success_url(self):
        return reverse('umanage_forgot_password_success')


class ForgotPasswordExpiredView(TemplateView):

    template_name = 'umanage/forgot_password/forgot_password_expired.html'


class ForgotPasswordChangeSuccessView(TemplateView):

    template_name = 'umanage/forgot_password/forgot_password_change_success.html'

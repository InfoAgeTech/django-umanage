from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth import get_user_model
from django.http.response import Http404
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.views.generic.base import View
from django_core.auth.views import AuthorizationTokenRequiredViewMixin

from ..models import AccountActivationAuthorization


class ActivateAccountView(AuthorizationTokenRequiredViewMixin, View):

    authorization_class = AccountActivationAuthorization

    def dispatch(self, request, *args, **kwargs):
        user = self.get_authorization_user()

        if user and user.is_active:
            return redirect('/')

        return super(ActivateAccountView, self).dispatch(request,
                                                         *args,
                                                         **kwargs)

    def get(self, request, *args, **kwargs):
        self.authorization.created_user.is_active = True
        self.authorization.created_user.save()

        self.authorization.expire()
        return redirect('umanage_activate_account_success')

    def get_authorization_user(self):
        User = get_user_model()
        try:
            user = User.objects.get(username=self.kwargs.get('username'))
        except User.DoesNotExist as e:
            raise Http404

        self.authorization_user = user
        return user


class ActivateAccountSuccessView(TemplateView):

    template_name = 'umanage/activate_account/activate_account_success.html'

    def get_context_data(self, **kwargs):
        context = super(ActivateAccountSuccessView,
                         self).get_context_data(**kwargs)
        context['login_url'] = getattr(settings, 'LOGIN_URL', '/login')
        return context


class ActivateAccountExpiredView(TemplateView):

    template_name = 'umanage/activate_account/activate_account_expired.html'

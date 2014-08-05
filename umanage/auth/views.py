from __future__ import unicode_literals

from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django_core.views.mixins.auth import LoginRequiredViewMixin
from django_core.views.mixins.csrf import CsrfExemptViewMixin


class LogoutView(CsrfExemptViewMixin, LoginRequiredViewMixin, TemplateView):

    template_name = 'umanage/auth/logout.html'

    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('/')

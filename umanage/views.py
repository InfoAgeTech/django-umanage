from __future__ import unicode_literals

from django.views.generic.base import TemplateView


class TokenExpiredView(TemplateView):

    template_name = 'umanage/token_expired.html'

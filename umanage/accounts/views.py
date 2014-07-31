from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django_core.utils.loading import get_class_from_settings_full_path
from django_core.views.mixins.auth import LoginRequiredViewMixin

from ..exceptions import UManageSettingImproperlyConfigured
from .forms import UserAccountForm


class AccountView(LoginRequiredViewMixin, TemplateView):

    template_name = 'umanage/accounts/account_view.html'

    def get_context_data(self, **kwargs):
        context = super(AccountView, self).get_context_data(**kwargs)
        user = self.request.user
        settings_key = 'UMANAGE_USER_ACCOUNT_DISPLAY_FIELDS'
        user_fields_to_display = getattr(settings,
                                         settings_key,
                                         ('first_name', 'last_name', 'email'))

        if not isinstance(user_fields_to_display, tuple):
            raise UManageSettingImproperlyConfigured(settings_key)

        fields_to_display = []

        for field_name in user_fields_to_display:
            try:
                val = getattr(user, field_name)
                label = user._meta.get_field_by_name(field_name)[0].verbose_name
            except:
                raise UManageSettingImproperlyConfigured(
                    settings_key,
                    message=_('"{0}" is not a valid field on the User model. '
                              'Check the "{1}" config '
                              'setting.').format(field_name, settings_key)
                )
            fields_to_display.append((label.title(), val))

        context['fields_to_display'] = fields_to_display
        return context


class AccountEditView(LoginRequiredViewMixin, FormView):

    template_name = 'umanage/accounts/account_edit.html'
    form_class = UserAccountForm

    def dispatch(self, *args, **kwargs):
        settings_key = 'UMANAGE_USER_ACCOUNT_EDIT_FORM'
        if hasattr(settings, settings_key):
            try:
                self.form_class = get_class_from_settings_full_path(settings_key)
            except:
                msg = _('{0} setting path is either incorrect or the app is '
                        'not installed.  Please check the '
                        'configuration.').format(settings_key)
                raise UManageSettingImproperlyConfigured(settings_key, msg)

        return super(AccountEditView, self).dispatch(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(AccountEditView, self).get_form_kwargs()
        kwargs['instance'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(AccountEditView, self).form_valid(form)

    def get_success_url(self):
        return reverse('umanage_account_view')

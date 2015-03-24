from django.core.urlresolvers import reverse
from django.shortcuts import redirect


class UsablePasswordRequiredMiddleware(object):
    """Middleware for requiring a user to have a usable password.

    If a user authenticates through a 3rd party, then django sets the password
    to an unusable password.  If this is the case, the user needs to set a
    password.
    """
    def process_request(self, request):
        user = request.user
        set_password_url = reverse('umanage_set_password')
        is_request_set_password_url = set_password_url in request.path

        if (user.is_authenticated() and
            not user.has_usable_password() and
            not is_request_set_password_url):

            # redirect user to set password
            return redirect(set_password_url)

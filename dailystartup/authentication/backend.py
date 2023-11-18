from agenda.models import SupportEngineer
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ObjectDoesNotExist


class StandUpBackend(BaseBackend):
    """
    Authenticate against the settings ADMIN_LOGIN and ADMIN_PASSWORD.

    Use the login name and a hash of the password. For example:

    ADMIN_LOGIN = 'admin'
    ADMIN_PASSWORD = 'pbkdf2_sha256$30000$Vo0VlMnkR4Bk$qEvtdyZRWTcOsCnI/oQ7fVOu1XAURIZYoOZ3iq8Dr4M='
    """

    def authenticate(self, request, username=None, password=None):
        """
        Overrides the authenticate method to allow users to log in using their email address.
        """
        print("Using Custome Backend")
        login_valid = settings.ADMIN_LOGIN == username
        pwd_valid = password == settings.ADMIN_PASSWORD
        if login_valid and pwd_valid:
            try:
                user = SupportEngineer.objects.get(username=username)
            except ObjectDoesNotExist:
                # Create a new user. There's no need to set a password
                # because only the password from settings.py is checked.
                user = SupportEngineer(username=username)
                user.is_staff = True
                user.is_superuser = True
                user.save()
            return user
        return None

    def get_user(self, user_id):
        """
        Overrides the get_user method to allow users to log in using their email address.
        """
        try:
            return SupportEngineer.objects.get(pk=user_id)
        except ObjectDoesNotExist:
            return None

from agenda.models import SupportEngineer
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist


class StandUpBackend(ModelBackend):
    """
    Authenticate against the settings ADMIN_LOGIN and ADMIN_PASSWORD.

    Use the login name and a hash of the password. For example:

    """

    def authenticate(self, request, username=None, password=None):
        """
        Overrides the authenticate method to allow users to log in.
        """
        
        print("Using Custom Backend")
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            return None
        if user.check_password(password):
            return user

    def get_user(self, username):
        """
        Overrides the get_user method to allow users to log in using their email address.
        """
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(username=username)
        except ObjectDoesNotExist:
            return None

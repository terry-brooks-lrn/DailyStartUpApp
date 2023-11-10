from django.forms import CharField, PasswordInput, Form
from django.utils.translation import gettext_lazy as _


class LoginForm(Form):
    username = CharField(label="Username", max_length=80, required=True)
    password = CharField(label="Password", widget=PasswordInput())

    class Meta:
        error_messages = {
            "username": {
                "max_length": _("This writer's name is too long."),
            },
        }

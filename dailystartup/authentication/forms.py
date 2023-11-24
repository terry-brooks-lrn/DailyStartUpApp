from django.forms import CharField, PasswordInput, Form, BooleanField
from django.utils.translation import gettext_lazy as _
from agenda.models import WIN_OOPS, Agenda, Item
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column
from crispy_forms.layout import HTML
from crispy_forms.layout import Layout, Div
from crispy_forms.layout import Row, Field, Button
from crispy_forms.bootstrap import FormActions
from django.urls import reverse
from captcha.fields import ReCaptchaField
from django.shortcuts import redirect


class LoginForm(Form):
    username = CharField(label="Username", max_length=80, required=True)
    password = CharField(label="Password", widget=PasswordInput())
    remember = BooleanField(label="Keep Me Logged In")
    # captcha = ReCaptchaField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "login-form"
        self.helper.layout = Layout(
            Row(
                Column("username", css_class="form-group col-md-6 mb-0"),
                Column("password", css_class="form-group col-md-6 mb-0"),
                css_class="form-row",
            ),
            Row("remember", css_class="form-row"),
            Row('captcha', css_class="form-row"),
            Row(
                FormActions(
                    Button(
                        "submit",
                        "Login",
                        css_class="btn btn-success",
                    ),
                    HTML('<a class="btn btn-danger" href="/auth/password_reset">Forgot Pasword</a>'),
                    css_class="modal-footer",
                ),
            ),
        )

    class Meta:
        fields = ("username", "password", "remember")

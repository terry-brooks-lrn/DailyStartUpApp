from django.contrib import messages
from agenda.models import WIN_OOPS, Agenda, Item, SupportEngineer, NOW
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login
import os
from logtail import LogtailHandler
from loguru import logger
from django.conf import settings
from authentication.forms import LoginForm

PRIMARY_LOG_FILE = os.path.join(settings.BASE_DIR, "standup", "logs", "primary_ops.log")
CRITICAL_LOG_FILE = os.path.join(settings.BASE_DIR, "standup", "logs", "fatal.log")
DEBUG_LOG_FILE = os.path.join(settings.BASE_DIR, "standup", "logs", "utility.log")
LOGTAIL_HANDLER = LogtailHandler(source_token=os.getenv("LOGTAIL_API_KEY"))

logger.add(DEBUG_LOG_FILE, diagnose=True, catch=True, backtrace=True, level="DEBUG")
logger.add(PRIMARY_LOG_FILE, diagnose=False, catch=True, backtrace=False, level="INFO")
logger.add(LOGTAIL_HANDLER, diagnose=False, catch=True, backtrace=False, level="INFO")


# SECTION - Login View


def login_user(request):
    if request.method == "POST":
        # form = LoginForm(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            redirect(to=reverse("home"))
        else:
            pass
    else:
        context = dict()
        context["form"] = LoginForm()
        return render(request, "registration/login.html", context)


# !SECTION

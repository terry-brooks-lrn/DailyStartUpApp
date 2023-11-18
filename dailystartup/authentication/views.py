# from django.contrib import messages
# from agenda.models import WIN_OOPS, Agenda, Item, SupportEngineer, NOW
# import os
# from logtail import LogtailHandler
# from loguru import logger
# from django.conf import settings
# from django.shortcuts import render, redirect, reverse
# from django.contrib.auth import authenticate, login, logout
# from authentication.forms import LoginForm
# from authentication.backend import StandUpBackend
# PRIMARY_LOG_FILE = os.path.join(settings.BASE_DIR, "standup", "logs", "primary_ops.log")
# CRITICAL_LOG_FILE = os.path.join(settings.BASE_DIR, "standup", "logs", "fatal.log")
# DEBUG_LOG_FILE = os.path.join(settings.BASE_DIR, "standup", "logs", "utility.log")
# LOGTAIL_HANDLER = LogtailHandler(source_token=os.getenv("LOGTAIL_API_KEY"))

# logger.add(DEBUG_LOG_FILE, diagnose=True, catch=True, backtrace=True, level="DEBUG")
# logger.add(PRIMARY_LOG_FILE, diagnose=False, catch=True, backtrace=False, level="INFO")
# logger.add(LOGTAIL_HANDLER, diagnose=False, catch=True, backtrace=False, level="INFO")


# # SECTION - Login View


# def signin(request):
#     """Sign in the user with the provided credentials.

#     Args:
#         request (HttpRequest): The HTTP request object.

#     Returns:
#         HttpResponse: A redirect response to the home page if the user is successfully authenticated,
#         otherwise a redirect response to the login page.

#     Raises:
#         None

#     Example:
#         signin(request)
#     """

#     if request.method == "post":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get("username")
#             password = form.cleaned_data.get("password")
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request=request, user=user)
#                 return redirect("home")
#             else:
#                 messages.success(message='Invaild Username and Password Combonation')
#                 return redirect('login')
#         else:
#             messages.success(message="Please Fix the Form Errors")
#             return redirect('login')
#     else:
#         context = dict()
#         context['form'] = LoginForm()
#         return render(request, 'registration/login.html', context)

#     def logout(request):
#         logout(request)

# # !SECTION

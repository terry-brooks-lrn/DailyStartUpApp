from django.urls import path
from authentication import views

urlpatterns = [path("log_me_in", views.login_user, name="login")]

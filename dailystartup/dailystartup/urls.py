"""
URL configuration for dailystartup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
import api.urls
import agenda.urls
import authentication.urls
from agenda.models import SupportEngineer
from django.urls import include, path, re_path
from rest_framework import routers, serializers, viewsets


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SupportEngineer
        fields = ["url", "username", "email", "is_staff"]


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = SupportEngineer.objects.all()
    serializer_class = UserSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r"users", UserViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(agenda.urls)),
    path("api", include(api.urls)),
    path("martor/", include("martor.urls")),
    path("auth/", include("django.contrib.auth.urls")),
    path("auth/", include("authentication.urls")),
    re_path(r"^ht/", include("health_check.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
]

from api import views
from django.urls import include, path
from django.views.decorators.cache import cache_page

urlpatterns = [
    path("api-auth/", include("rest_framework.urls")),
    path(
        "agenda/",
        cache_page(timeout=43200, key_prefix="api")(views.AgendasViews.as_view()),
        name="home-page",
    ),
    path("agenda/<str:date>", views.AgendaView.as_view()),
    path("item/<int:id>", views.ItemViews.as_view(), name="single_item"),
    path(
        "items/",
        cache_page(timeout=43200, key_prefix="api")(views.ItemsViews.as_view()),
        name="create_list_items",
    ),
]


handler500 = "rest_framework.exceptions.server_error"
handler400 = "rest_framework.exceptions.bad_request"

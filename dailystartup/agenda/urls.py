from agenda import views
from django.urls import path
from django.views.decorators.cache import cache_page

urlpatterns = [
    # SECTION -  Template Rendering URLs
    path("", cache_page(timeout=60, key_prefix="agenda")(views.root), name="home"),
    path(
        "support-mail",
        cache_page(timeout=60, key_prefix="supportmail")(views.supportmail),
        name="support-mail",
    ),
    path(
        "item-log",
        cache_page(timeout=60, key_prefix="log")(views.item_log),
        name="item-log",
    ),
    # SECTION - AJAX Hook URLs
    path("get-item-detail", views.get_item_details, name="get-item-details"),
    path("solve-item", views.resolve_item, name="solve-item"),
    path("feat-accepted", views.mark_feat_accepted, name="mark-feat-accepted"),
    path("feat-rejected", views.mark_feat_rejected, name="mark-feat-rejected"),
    path("reopen", views.reopen_item, name="reopen-item"),
    path("convert", views.convert_to_fyi, name="move-to-monitoring"),
]

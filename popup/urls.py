from django.urls import path
from . import popup_views

urlpatterns = [
    path(
        "save-visitor/",
        popup_views.save_visitor,
        name="save_visitor",
    ),
]
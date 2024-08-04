from django.urls import path

from . import views
from .views import render_markdown, search_markdown

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name='add'),
    path("entries/", views.save, name='save'),
    path('<str:filename>', render_markdown, name='render_markdown'),
    path('entries/', search_markdown, name='search_markdown'),
]

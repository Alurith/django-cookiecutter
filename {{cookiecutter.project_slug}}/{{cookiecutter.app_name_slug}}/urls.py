from django.urls import path

from .views import HomepageView

app_name = "{{cookiecutter.app_name_slug}}"
urlpatterns = [
    path("", HomepageView.as_view(), name="homepage"),
]

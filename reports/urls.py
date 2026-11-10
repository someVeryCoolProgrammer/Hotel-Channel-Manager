from django.urls import path

from .views import Views

urlpatterns = [
    path("", Views.home_page, name=""),
    path("report", Views.report, name="report"),
]

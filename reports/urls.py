from django.urls import path

from .views import Views

urlpatterns = [
    path("", Views.home_page, name=""),
    path("managers-report", Views.managers_report, name="managers-report"),
    path("owners-report", Views.owners_report, name="owners-report"),
]

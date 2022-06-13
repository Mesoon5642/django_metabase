from django.urls import path
from . import views

urlpatterns = [
    path("submit_report/", views.submit_report, name="submit_report"),
    path("thanks/", views.thanks, name="thanks")
]

from django.urls import path
from . import views
from django.views.i18n import JavaScriptCatalog

app_name = "MetaApp"
urlpatterns = [
    path("submit_report/", views.submit_report, name="submit_report"),
    path("thanks/", views.thanks, name="thanks"),
    path("", views.index, name="index"),
    path("viewdata/", views.viewdata, name="viewdata"),
    path("login/", views.login, name="login"),
    path("createaccount/", views.create, name="create"),
    path("viewreports/", views.viewreports, name="viewreports"),
    path("viewdetail/<str:reportname>", views.viewdetail, name="viewdetail")
]

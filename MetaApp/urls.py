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
    path("viewdetail/<int:rid>", views.viewdetail, name="viewdetail"),
    path("addevidence/<int:rid>", views.addevidence, name="addevidence"),
    path("addsuspect/<int:rid>", views.addsuspect, name="addsuspect"),
    path("addlocation/<int:rid>", views.addlocation, name="addlocation"),
    path("addsuspect/<int:rid>/addevidence/<int:sid>", views.susaddevidence, name="addsuspect"),
    path("addsuspect/<int:rid>/addlocation/<int:sid>", views.susaddlocation, name="addsuspect"),
    path("suspectdetail/<int:sid>", views.suspectdetail, name="suspectdetail"), 
    path("deletereport/<int:rid>", views.deletereport, name="deletereport"), 
    path("deleteevidence/<int:eid>", views.deleteevidence, name="deleteevidence"),
    path("deletelocation/<int:lid>", views.deletelocation, name="deletelocation"),
    path("deletesuspect/<int:sid>", views.deletesuspect, name="deletesuspect"),
]

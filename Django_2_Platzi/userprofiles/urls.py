from django.urls import path
from . import views

app_name = 'userprofiles'

urlpatterns = [
    path("login", views.authentication, name="authentication"),
    path("logout", views.logout_view, name="logout")
]

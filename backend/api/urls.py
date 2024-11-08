from django.urls import path
from . import views

urlpatterns = [
    path("chat/", views.CreateQuestion.as_view(), name="question"),
    #path("new_page", views.CreateLinkClick.as_view(), name="link"),
] 
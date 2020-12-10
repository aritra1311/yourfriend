from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('board', views.board, name="board"),
    path('contact-us', views.contactUs, name="contactUs"),
    path('campaigns', views.campaigns, name="campaigns"),
    path('internship', views.internship, name="internship"),
    path('mental', views.mental, name="mental"),
    path('webinar', views.webinar, name="webinar"),
]
from django.urls import path
from episodes.views import show_home, show_about, show_contact

urlpatterns = [
    path('home/', show_home, name="show_home"),
    path('home/about/', show_about, name="show_about"),
    path('home/contact/', show_contact, name="show_contact")
]

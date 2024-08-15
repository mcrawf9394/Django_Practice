from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.say_hello, name="Hello"),
    path("other/", views.anotherFun, name="Other"),
]
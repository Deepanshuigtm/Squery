from django.urls import path
from . import views

urlpatterns = [
    path("",views.startingpage, name = "starting-page"),
    path("query",views.querys, name = "querys"),

]
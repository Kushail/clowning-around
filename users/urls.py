from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name='index')                  #'' means root of this app, #note that we were not calling the views.index function but just passing a reference to it as an argument into path
]
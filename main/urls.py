from django.urls import path
from . import views

app_name = "main"   

urlpatterns = [
  path("", views.homepage, name="homepage"),
  path('welcomes/',views.welcomes, name="welcomes")
  
  
  
  
]
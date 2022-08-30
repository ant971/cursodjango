from django.urls import path
from .views import centromedicoListView
app_name= "centromedico"
urlpatterns = [
    path('', centromedicoListView.as_view(), name="home") 
]
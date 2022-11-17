from django.urls import path
from . import views

app_name = "port"
urlpatterns =[
    path('index/', views.index, name="index")
]
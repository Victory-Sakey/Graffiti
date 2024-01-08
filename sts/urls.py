from django.urls import path
from .import views



app_name = 'sts'


urlpatterns = [
    path('', views.sts ,  name='sts'),
]


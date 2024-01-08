from django.urls import path
from .views import Graffiti,JoinCommunity,Success



app_name = 'Graffiti'


urlpatterns = [
    path('', Graffiti , name='Graffiti'),
    path('JoinCommunity', JoinCommunity , name='JoinCommunity'),
    path('Success/<str:jc_name>/', Success, name='Success')
]


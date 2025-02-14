from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('register/',register,name='register'),
    path('user_login/',user_login,name='user_login'),
    path('user_logout/',user_logout,name='user_logout'),
    path('create_contact/',create_contact,name='create_contact'),
    path('display<pk>/',display,name='display'),
    path('update<pk>/',update,name='update'),
    path('delete<pk>/',delete,name='delete'),
    path('search',search,name='search')
]


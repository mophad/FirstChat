from django.urls import path
from . import views

urlpatterns = [
    path('' ,views.login , name = 'login'),
    path('user', views.user, name='user'),
    path('forgot', views.forgot,)
]
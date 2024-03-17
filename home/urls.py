from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('login', views.LoginInterfaceView.as_view(), name='login'),
    # TODO: logout page returns 405
    path('logout', views.LogoutInterfaceView.as_view(), name='logout'),
]
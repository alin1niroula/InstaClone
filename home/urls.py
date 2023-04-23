from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('',views.home,name="home"),
    path('createprofile/',views.create_profile,name="signup"),
    path('login/',views.Login,name="Login"),
    path('profile/',views.profile,name="profile"),
]
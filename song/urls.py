from django.urls import path
from . import views

app_name = "App"
urlpatterns = [
    path('index', views.index, name="index"),
    path('', views.home, name='home'),
    path('signup', views.signuplogin, name="signup_login"),
    path('login', views.login),
    path('logout/', views.handlelogout, name="logout"),
    path('user_login/', views.user_login)

]

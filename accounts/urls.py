from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signup/success/', views.signup_success, name='signup_success'),
    path('signup/failure/', views.signup_failure, name='signup_failure'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
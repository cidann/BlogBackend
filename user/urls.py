from django.urls import path
from . import views

urlpatterns=[
    path('users/',views.UserList.as_view()),
    path('users/<int:id>/', views.UserDetails.as_view()),
    path('users/auth/login',views.UserLogin.as_view()),
]
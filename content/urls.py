from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('',views.index),
    path('blogs/',views.BlogList.as_view()),
    path('blogs/<int:id>/', views.BlogDetails.as_view()),
]
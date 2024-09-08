from django.urls import path
from . import views

urlpatterns = [
    path('',views.coreHome, name='coreHome'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('cats/', views.hello_cats, name='hello_cats'),
]
from django.urls import path

from . import views

urlpatterns = [
    # uses home function in the view.py
    path('', views.home, name='home'),
    # uses add function in the view.py
    path('add', views.add, name='add')
]
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addchecks/', views.addchecks, name='addchecks'),
    path('editcheck/', views.editcheck, name='edit'),
    path('submitcheck/', views.submit, name='submit'),
]
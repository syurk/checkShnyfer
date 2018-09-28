from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addchecks/', views.addchecks, name='addchecks'),
    path('editcheck/', views.editcheck, name='editcheck'),
    path('deletecheck/', views.deletecheck, name='deletecheck'),
    path('submitcheck/', views.submit, name='submit'),
]
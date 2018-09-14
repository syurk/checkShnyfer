from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submitcheck/', views.submit, name='submitcheck'),
    path('viewchecks/', views.viewchecks, name='viewchecks'),
]
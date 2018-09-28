from django.urls import path

from . import views

app_name = 'addchecks_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('submitcheck/', views.submit, name='submitcheck'),
    path('viewchecks/', views.viewchecks, name='viewchecks'),
]
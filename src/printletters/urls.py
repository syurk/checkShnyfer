from django.urls import path

from . import views

app_name = 'printletters_app'

urlpatterns = [
    path('', views.index, name='index'),
    path(r'download/', views.download, name='download')
]
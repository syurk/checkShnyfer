from django.urls import path

from . import views

app_name = 'printletters_app'

urlpatterns = [
    path('', views.index, name='index'),
    path(r'download/\?(id=[0-9]+)+', views.download, name='download')
]
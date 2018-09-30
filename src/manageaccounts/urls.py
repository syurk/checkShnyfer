from django.urls import path

from . import views

app_name = 'manageaccounts_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('addaccount/', views.addaccounts, name='addaccount'),
    path('editaccount/', views.editaccount, name='editcheck'),
    path('deleteaccount/', views.deleteaccount, name='deleteaccount'),
    path('submitaccount/', views.submit, name='submit'),
]
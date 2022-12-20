from django.urls import path

from fitness import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('trainings/<str:string>', views.index, name='trainings'),
    path('signUp/', views.signUp_link, name='signUp'),
    path('signIn/', views.signIn_link, name='signIn'),
    path('checkmail', views.checkmail),
    path('logout', views.logoutUser),
    path('enrollForm/', views.enrollForm, name='enrollForm'),
    path('personalTraining/', views.personalTraining, name='personalTraining'),
    path('enrollGroup/', views.enrollGroup, name='enrollGroup'),
    path('groupTraining/', views.groupTraining, name='groupTraining'),
    path('password_change/', views. PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('index2/', views.index2, name='index2'),
    path('', views.index, name='Index'),
]
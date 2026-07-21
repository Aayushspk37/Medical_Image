from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index,name="index"),
    path('dashboard/', views.home,name="dashboard"),
    path('index/',views.index,name="index"),
    path('about/', views.about,name="AboutUs"),
    #path('diagnosis/', views.Crop_recommend,name="diagnosis"),
    path('services/', views.services,name="Services"),
    path('contact/', views.contact ,name="contact"),
    path('login/', views.user_login ,name="login"),
    #path('logout/', views.user_logout ,name="logout"),
    path('terms/', views.terms ,name="terms"),
    path('result/', views.result ,name="result"),
    path('faq/', views.faq ,name="faq"),
    path('metrics/', views.metrics ,name="metrics"),
    path('modalities/', views.modalities ,name="modalities"),
    path('pricing/', views.pricing ,name="pricing"),
    path('privacy/', views.privacy ,name="privacy"),
    path('register/', views.register ,name="register"),
    path('report/', views.report ,name="report"),
    path('reports/', views.reports ,name="reports"),
    path('research/', views.research ,name="research"),
    path('support/', views.support ,name="support"),
    path('team/', views.team ,name="team"),
    path('documentation/', views.documentation,name="Documentation"),
    path('history/', views.history, name='history'),
    #path('history/delete/', views.delete_history, name='delete_history'),
]
    
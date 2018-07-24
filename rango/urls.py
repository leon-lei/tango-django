from django.urls import path

from . import views

app_name='rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_category/', views.add_category, name='add_category'),
    path('category/<slug:slug>/add_page/', views.add_page, name='add_page'),
    path('category/<slug:slug>/', views.category, name='category'),
    # path('register/', views.register, name='register'),
    # path('login/', views.user_login, name='login'),
    # path('logout/', views.user_logout, name='logout'),
    path('restricted/', views.restricted, name='restricted'),
]

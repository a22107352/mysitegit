
from django.urls import path

from . import views

urlpatterns = [

    path('', views.projeto_cadeira_list, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout', views.logout_view,name='logout'),
    path('create/', views.projeto_cadeira_create, name='create'),
    path('delete/<str:obj_type>/<str:obj_id>/', views.projeto_cadeira_delete, name='projeto_cadeira_delete'),

]

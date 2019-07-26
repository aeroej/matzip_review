from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('comment/', views.comment, name='comment'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
    path('co_update/', views.co_update, name='co_update'),
    path('co_delete/', views.co_delete, name='co_delete'),
]
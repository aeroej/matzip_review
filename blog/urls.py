from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:blod_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('update/<int:blod_id>/', views.update, name='update'),
    path('delete/<int:blod_id>/', views.delete, name='delete'),
    path('comment/<int:post_id>/', views.comment, name='comment'),
    path('co_update/<int:post_id>/', views.co_update, name='co_update'),
    path('co_delete/<int:post_id>/', views.co_delete, name='co_delete'),
]
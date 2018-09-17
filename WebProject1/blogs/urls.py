from django.urls import path

from . import views

app_name = 'blogs'

urlpatterns = [
    # ex: /
    path('', views.index, name='index'),
    # ex: /post/create/
    path('post/create/', views.create, name='create'),
    # ex: /post/1/
    path('post/<int:pk>/', views.detail, name='detail'),
    # ex: /post/1/update/
    path('post/<int:pk>/update/', views.update, name='update'),
    # ex: /post/1/delete
    path('post/<int:pk>/delete/', views.delete, name='delete'),
]

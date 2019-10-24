from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name="create"),
    path('hashtags/<int:id>/', views.hashtags, name="hashtags"),
    path('like/<int:id>/', views.like, name="like"),
    path('delete/<int:id>/', views.delete, name="delete"),
    path('update/<int:id>/', views.update, name="update"),
    path('<int:id>/', views.detail, name="detail"),
    path('<int:id>/create_comment', views.create_comment, name="create_comment"),
    
]

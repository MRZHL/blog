from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:pk>/', views.detail, name='detail'),
]

# 这个重要 一定要加上这句
app_name = "TestModel"

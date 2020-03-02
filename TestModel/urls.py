from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:pk>/', views.detail, name='detail'),
    path('archives/<int:year>/<int:month>/', views.archive, name="archive"),  # 这个 archive 在html中的路径中
    path('categories/<int:pk>/', views.category, name="category"),
    path('tags/<int:pk>/', views.tag, name="tag"),
]

# 这个重要 一定要加上这句
app_name = "blog"

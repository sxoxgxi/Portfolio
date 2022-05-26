from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('blog/', views.blog, name="blog"),
    path('blog/<str:id>', views.blog_detail, name="blog_detail"),
]

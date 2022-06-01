from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('blog/', views.blog, name="blog"),
    path('blog/<str:id>', views.blog_detail, name="blog_detail"),
    path('login/', views.loginView, name="login"),
    path('register/', views.registerView, name="register"),
    path('logout/', views.logoutView, name="logout"),
    path('profile/<str:id>', views.profileView, name="profile"),
]

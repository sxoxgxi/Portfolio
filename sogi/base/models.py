from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# class User(AbstractUser):
#     name = models.CharField(max_length=255, null=True)
#     email = models.EmailField(unique=True, null=True)
#     bio = models.TextField(null=True)
#     # avatar = models.ImageField(null=True)
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created', '-updated']

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created', '-updated']

    def __str__(self) -> str:
        return self.body

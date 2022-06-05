from django.forms import ModelForm
from .models import User, Post
from django.contrib.auth.forms import UserCreationForm


class MyUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        
class Blog(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
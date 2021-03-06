from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from accounts.models import Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('post',)
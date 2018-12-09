from django import forms
from .models import Post, Comments

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ["comments_text"]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["post_title", "post_text"]

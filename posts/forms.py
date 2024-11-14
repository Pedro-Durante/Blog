from django import forms
from .  import models

class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title','body','banner','slug']

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = [
            'body',
        ]
        labels = {
            'body': 'Comment',
        }
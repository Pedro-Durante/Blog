from django import forms
from .  import models

class CreatePost(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=models.Category.objects.all())
    class Meta:
        model = models.Post
        fields = ['title','body','banner','slug','categories']

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = [
            'body',
        ]
        labels = {
            'body': 'Comment',
        }
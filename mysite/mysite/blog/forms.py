from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'conteudo')


class CommentForm(forms.Form):
    post_id = forms.IntegerField(widget=forms.HiddenInput())
    conteudo = forms.CharField(widget=forms.Textarea)

from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'text')


class LoginForm(forms.Form):
	user = forms.CharField(max_length=100)
	password = forms.CharField(widget=forms.PasswordInput())


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
from django import forms

from .models import Post, Comment

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('title', 'text',)


class CommentForm(forms.ModelForm):
	# name = forms.CharField()
	# email = forms.EmailField()
	# comment = forms.CharField(widget=forms.Textarea)

	class Meta:
		model = Comment
		fields = ('name', 'email', 'comment')
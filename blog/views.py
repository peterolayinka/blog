from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import PostForm, CommentForm

from .models import Post, Comment

# Create your views here.

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'blog/post_list.html',{'posts': posts})

def post_detail(request, post_id):
	post_data = get_object_or_404(Post, pk=post_id)
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			print('Good form data')
			Comment = form.save(commit=False)
			Comment.post_id = post_data
			Comment.save() 
			return redirect('post_detail', post_id=post_id)
	else:
		form = CommentForm()

	return render(request, 'blog/post_detail.html', {'post_data': post_data, 'form': form} )

def post_new(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', post_id=post.pk)
	else:
		form = PostForm()

	return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	if request.method == 'POST':
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('post_detail', post_id=post.pk)
	else:
		form = PostForm(instance=post)

	return render(request, 'blog/post_edit.html', {'form': form})


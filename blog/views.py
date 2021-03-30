from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from blog.models import Post, Tag
from blog.forms import PostForm, CommentForm, RegisterForm

# Create your views here.

def post_list(request):
  posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
  return render(request, 'blog/post_list.html', {'posts': posts})

def post_list_filtered(request, tag):
  posts = Post.objects.filter(published_date__lte=timezone.now(), tags__text=tag).order_by('-published_date')
  return render(request, 'blog/post_list.html', {'posts': posts, 'page_title': tag.capitalize()})

def post_detail(request, pk):
  post = get_object_or_404(Post, pk=pk)
  if request.method == 'POST':
    form = CommentForm(request.POST)
    if form.is_valid():
      new_comment = form.save(commit=False)
      new_comment.author = request.user
      new_comment.post = post
      new_comment.created_date = timezone.now()
      new_comment.save()
      return redirect('post_detail', pk=post.pk)
  else:
    form = CommentForm()
    return render(request, 'blog/post_detail.html', {'post': post, 'form': form})

@login_required
def post_new(request):
  if request.method == 'POST':
    form = PostForm(request.POST)
    if form.is_valid():
      post = form.save(commit=False)
      post.author = request.user
      post.published_date = timezone.now()
      post.save()
      post.tags.set(Tag.objects.filter(pk__in=request.POST.getlist('tags')))
      post.save()
      return redirect('post_detail', pk=post.pk)

  else:
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
  post = get_object_or_404(Post, pk=pk)
  if request.method == 'POST':
    form = PostForm(request.POST, instance=post)
    if form.is_valid():
      post = form.save(commit=False)
      post.author = request.user
      post.tags.set(Tag.objects.filter(pk__in=request.POST.getlist('tags')))
      post.save()
      return redirect('post_detail', pk=post.pk)
  else:
    form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def register(request):
  if request.method == 'POST':
    form = RegisterForm(request.POST)
    if form.is_valid():
      try:
        user = User.objects.create_user(request.POST['username'], password=request.POST['password'])
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.save()
        return redirect('login')
      except:
        return render(request, 'registration/register.html', {'form': form, 'error': 'Something happened, please try again'})
  else:
    form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})
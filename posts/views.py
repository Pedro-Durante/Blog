from django.shortcuts import render,redirect, get_object_or_404, get_list_or_404
from .models import Post, Comment, Category
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from . import forms
from .forms import CreatePost
# Create your views here.
def posts_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request,'posts/posts_list.html',{ 'posts': posts })

def post_page(request,slug):
    post = Post.objects.get(slug=slug)
    post_id = post.id
    comments = Comment.objects.filter(post=post_id).order_by('-date')
    cats = post.categories.all()
    return render(request,'posts/post_page.html',{ 'post': post, 'cats' : cats, 'comments': comments })

def update_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == "POST":
        form = CreatePost(request.POST)
        if form.is_valid():
            post.title = request.POST['title']
            post.date = post.date
            post.banner = request.POST['banner']
            post.body = request.POST['body']
            post.categories.set(form.cleaned_data.get("categories"))
            post.save()
            return redirect("posts:page", slug = slug)

    else:
        form = CreatePost(
            initial={
                "title": post.title,
                "date": post.date,
                "body": post.body,
                "slug": post.slug,
                "banner": post.banner,
            }
        )

    context = {"post": post, "form": form}
    return render(request, "posts/update.html", context)

def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        post.delete()
        return HttpResponseRedirect(reverse("posts:list"))

    context = {"post": post}
    return render(request, "posts/delete.html", context)



@login_required(login_url = "/users/login/")
def post_new(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.save()
            newpost.categories.set(form.cleaned_data.get("categories"))
            newpost.save()
            return redirect('posts:list')
    else:
        form = forms.CreatePost()
    return render(request, 'posts/post_new.html', {'form': form})

@login_required(login_url="/users/login")
def create_comment(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post_id = post_id = post.id
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment_author = request.user
            comment_text = form.cleaned_data['body']
            comment = Comment(author=comment_author,
                            body=comment_text,
                            post=post)
            comment.save()
            return redirect("posts:page", slug=slug)
    else:
        form = forms.CommentForm()
    comments = Comment.objects.filter(post=post_id).order_by('-date')
    return render(request, 'posts/comment.html', {'form': form, 'post': post, 'comments': comments})

def category(request, cat_id):
    posts = get_list_or_404(Post,categories=cat_id)
    cat = Category.objects.get(pk=cat_id)
    return render(request, 'posts/category.html', {'posts': posts, 'cat': cat})

def categories_list(request):
    cats = Category.objects.all()
    return render(request, 'posts/categories_list.html', {'cats': cats})


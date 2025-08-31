# posts/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm


def home(request):
    return HttpResponse("Hello, world!")


def post_list(request):
    """
    View to display a list of all posts.
    """
    posts = Post.objects.all().order_by("-created_at")  # newest first
    context = {
        "posts": posts,
        "page_title": "List of Posts",
    }
    return render(request, "posts/post_list.html", context)


def post_detail(request, pk):
    """
    View to display details of a specific post.
    """
    post = get_object_or_404(Post, pk=pk)
    return render(request, "posts/post_detail.html", {"post": post})


def post_create(request):
    """
    View to create a new post.
    """
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()  # PostForm handles assigning the author
            return redirect("post_list")
    else:
        form = PostForm()

    return render(request, "posts/post_form.html", {"form": form})


def post_update(request, pk):
    """
    View to update an existing post.
    """
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()  # use form.save() so author is handled correctly
            return redirect("post_list")
    else:
        form = PostForm(instance=post)

    return render(request, "posts/post_form.html", {"form": form})


def post_delete(request, pk):
    """
    View to delete an existing post.
    """
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect("post_list")

from django.shortcuts import render
from posts.models import Author, Topic, Post

def home_view(request):
    posts = Post.objects.all().filter(featured=True, archived=False)
    topics = Topic.objects.all()
    authors = Author.objects.all()
    context = {
        'posts': posts,
        'topics': topics,
        'authors': authors,
    }
    return render(request, 'index.html', context)
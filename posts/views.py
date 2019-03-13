from django.shortcuts import render, get_object_or_404
from .models import Author, Topic, Post

def topic_posts(request, id, slug):
    topics = Topic.objects.all()
    topic = get_object_or_404(Topic, id=id, slug=slug)
    topic_posts = topic.post_set.all()
    authors = Author.objects.all()
    context = {
        'authors': authors,
        'topics':topics,
        'topic': topic,
        'topic_posts': topic_posts
    }
    return render(request, 'posts/post_list.html', context)
def author_posts(request, id, slug):
    topics = Topic.objects.all()
    authors = Author.objects.all()
    author = get_object_or_404(Author, id=id, slug=slug)
    author_posts = Post.objects.filter(author__slug=slug)
    context = {
        'topics':topics,
        'author': author,
        'author_posts': author_posts,
        'authors': authors,
    }
    return render(request, 'posts/author_posts.html', context)
def post_detail(request, id, category, slug):
    topics = Topic. objects.all()
    posts = Post.objects.all().filter(latest=True)
    post = get_object_or_404(Post, id=id, category=category, slug=slug)
    authors = Author.objects.all()
    context = {
        'topics': topics,
        'posts': 'posts',
        'post': post,
        'authors': authors,
    }
    return render(request, 'posts/post_detail.html', context)
def article_reviews(request):
    article_reviews = Post.objects.filter(category='Article-Review')
    topics = Topic.objects.all()
    authors = Author.objects.all()
    context = {
        'article_reviews': article_reviews,
        'topics': topics,
        'authors': authors,
    }
    return render(request, 'posts/article_reviews.html', context)
def book_reviews(request):
    book_reviews = Post.objects.filter(category='Book-Review')
    topics = Topic.objects.all()
    authors = Author.objects.all()
    context = {
        'book_reviews': book_reviews,
        'topics': topics,
        'authors': authors,
    }
    return render(request, 'posts/book_reviews.html', context)

def commentaries(request):
    commentaries = Post.objects.filter(category='Commentary')
    topics = Topic.objects.all()
    authors = Author.objects.all()
    context = {
        'commentaries': commentaries,
        'topics': topics,
        'authors': authors,
    }
    return render(request, 'posts/commentaries.html', context)


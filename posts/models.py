from django.db import models
from django.shortcuts import reverse

class Author(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    class Meta:
        ordering = ('name',)
    def __str__(self):
        return self.name

class Topic(models.Model):
    name = models.CharField(max_length = 40)
    slug = models.SlugField(max_length=40)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('topic_posts', args=[str(self.id), self.slug])

class Post(models.Model):
    CATEGORY_CHOICES = (
        ('Article-Review', 'Article-Review'),
        ('Book-Review', 'Book-Review'),
        ('Commentary', 'Commentary'),
        ('About', 'About')
    )
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    latest = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    archived = models.BooleanField(default=False)
    topics = models.ManyToManyField(Topic)
    thumbnail = models.ImageField(upload_to='photos/posts/%Y', blank=True, null=True, default=None)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('posted_date', 'title', 'author')
    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id), self.category, self.slug])


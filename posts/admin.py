from django.contrib import admin
from .models import Author, Topic, Post

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name',]
    prepopulated_fields = {'slug': ('name',),}
    list_display_links = ['name',]

admin.site.register(Author, AuthorAdmin)

class TopicAdmin(admin.ModelAdmin):
    list_display = ['name',]
    prepopulated_fields = {'slug': ('name',),}
    list_display_links = ['name',]
admin.site.register(Topic, TopicAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'posted_date', 'featured', 'latest', 'archived']
    list_display_links = ['title', 'author']
    list_editable = ['featured', 'latest', 'archived']
    list_filter = ['author', 'category', 'featured', 'latest', 'archived']
    prepopulated_fields = {'slug': ('title',),}
admin.site.register(Post, PostAdmin)

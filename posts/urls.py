from django.urls import path
from . import views

urlpatterns = [
    path('topic_posts/<id>/<slug>/', views.topic_posts, name='topic_posts'),
    path('<id>/<category>/<slug>/', views.post_detail, name='post_detail'),
    path('<id>/<slug>/', views.author_posts, name='author_posts'),
    path('article_reviews/', views.article_reviews, name='article_reviews'),
    path('book_reviews/', views.book_reviews, name='book_reviews'),
    path('commentaries/', views.commentaries, name='commentaries'),
]
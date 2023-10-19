from . import views
from django.urls import path


urlpatterns = [
    path('blog/', views.allBlogPost, name='all_blog'),
    path('<slug:slug>/', views.post_detail, name='blog_post_detail'),
    path('add/', views.add_blog_post, name='add_blog_post'),
    path('edit/<slug:slug>/', views.edit_blog_post, name='edit_blog_post'),
    path('delete/<slug:slug>/', views.delete_blog_post, name='delete_blog_post'),
    
]
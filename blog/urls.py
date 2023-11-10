from . import views
from django.urls import path


urlpatterns = [
    path('blog/', views.AllBlogPost.as_view(), name='all_blog'),
    path('blog/<str:category>/', views.AllBlogPost.as_view(), name='all_blog'),
    path('add_post/', views.create_post, name='add_post'),  
    path('<slug:slug>/', views.PostDetail.as_view(), name='blog_post_detail'),
    path('blog/edit/<slug:slug>/', views.edit_blog_post, name='edit_blog_post'), 
    path('delete_blog_post/<int:pk>/', views.delete_blog_post, name='delete_blog_post'),
]
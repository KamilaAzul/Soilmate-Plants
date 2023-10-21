from . import views
from django.urls import path


urlpatterns = [
   
    path('blog/', views.AllBlogPost.as_view(), name='all_blog'),
    path('add_post/', views.create_post, name='add_post'),  
    path('<slug:slug>/', views.PostDetail.as_view(), name='blog_post_detail'),
    path('edit/<slug:slug>/', views.edit_blog_post, name='edit_blog_post'), 
]
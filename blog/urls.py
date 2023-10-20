from . import views
from django.urls import path


urlpatterns = [
   
    path('blog/', views.AllBlogPost.as_view(), name='all_blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='blog_post_detail'),
    
]
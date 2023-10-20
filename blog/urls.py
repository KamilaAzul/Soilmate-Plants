from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('blog/', views.AllBlogPost.as_view(), name='all_blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='blog_post_detail'),
    
]
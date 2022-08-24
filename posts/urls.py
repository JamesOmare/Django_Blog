from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='posts_home'),
    path('greet/', views.greet, name='greet_name'),
    path('posts/', views.return_all_posts, name='all_posts'),
    path('posts/<int:post_id>/', views.return_one_post, name='get_one_post'),
    path('about/', views.about, name='posts_about'),
    path('services/', views.services, name='posts_services'),
    path('create_post', views.create_post, name='create_post'),
    path('post/<int:post_id>', views.post_detail, name='post_detail' ),
    path('post/update/<int:post_id>', views.update_post, name='update_post')
]
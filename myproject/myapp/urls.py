from django.urls import path
from . import views

urlpatterns = [
	path('',views.get_posts_by_paginator_redirector),
	path('art', views.PostList, name='list'),
	path('art/<int:id>', views.get_posts_by_paginator, name='list3'),
	path('post/<str:title>/', views.get_posts_by_tags, name='tag_detail_url'),
	path('create', views.create_new_post, name = 'create'),
	path('createpost',views.create_post, name = 'create_post'),
	path('cc/<int:id>',views.delete_post_by_id, name = 'cr'),
]
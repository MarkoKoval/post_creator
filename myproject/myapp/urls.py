from django.urls import path
from . import views

urlpatterns = [
	path('',views.get_posts_by_paginator_redirector),
	path('page', views.handle_form, name='list'),
	path('page/<int:id>', views.get_posts_by_paginator, name='get_posts_by_paginator'),
	path('post/<str:title>/', views.get_posts_by_tags, name='tag_detail_url'),
	path('create', views.create_new_post, name='create'),
	path('delete/<int:id>', views.delete_post_by_id, name='delete'),
]
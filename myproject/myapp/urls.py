from django.urls import path
from . import views

urlpatterns = [
	path('',views.redirector),
	path('art', views.PostList, name='list'),
	path('art/<int:id>', views.GetP, name='list3'),
	path('page/<int:id>', views.listing, name='page'),
	path('post/<str:title>/', views.post_detail, name='tag_detail_url'),
	path('ref', views.aj, name = 'aj'),
	path('create', views.render_create_post, name = 'create'),
	path('createpost',views.create_post, name = 'create_post'),
	path('cc/<int:id>',views.cr, name = 'cr'),
]
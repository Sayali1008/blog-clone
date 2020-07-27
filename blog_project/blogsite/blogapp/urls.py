from django.conf.urls import url
from blogapp import views

urlpatterns = [
    url(r'^$',views.PostListView.as_view(), name='post_list'), # home page
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^post/create/$', views.CreatePostView.as_view(), name='post_create'),
    url(r'^post/(?P<pk>\d+)/update/$', views.UpdatePostView.as_view(), name='post_update'),
    url(r'^post/(?P<pk>\d+)/delete/$', views.DeletePostView.as_view(), name='post_delete'),
    url(r'^post/drafts/$', views.DraftListView.as_view(), name='post_drafts'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^post/(?P<pk>\d+)/comment/approve/$', views.approve_comments, name='approve_comments'),
    url(r'^post/(?P<pk>\d+)/comment/delete/$', views.remove_comments, name='remove_comments'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.publish_post, name='publish_post'),
]
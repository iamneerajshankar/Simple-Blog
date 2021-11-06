from django.urls import path
from blogApp.views import PostDetail, PostList, UpdateDetailView, add_post_view, DeleterDetailView

urlpatterns = [
    path('', PostList.as_view(), name='post-list'),
    path('article/<int:pk>', PostDetail.as_view(), name="article-details"),
    path('add_post/', add_post_view.as_view(), name='add-post'),
    path('article/edit/<int:pk>', UpdateDetailView.as_view(), name="update-post"),
    path('article/edit/<int:pk>/delete', DeleterDetailView.as_view(), name='delete-post')
]

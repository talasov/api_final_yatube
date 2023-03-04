from rest_framework import routers
from django.urls import path, include
from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet

v1_router = routers.DefaultRouter()

v1_router.register(r'posts', PostViewSet)
v1_router.register(r'groups', GroupViewSet)
v1_router.register(r'follow', FollowViewSet)
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('', include(v1_router.urls)),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]

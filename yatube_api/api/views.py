from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination
from .permissions import IsAuthorOrReadOnly, IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework import filters, status, viewsets

from posts.models import Follow, Group, Post, User
from .serializers import (
    CommentSerializer, FollowSerializer, GroupSerializer, PostSerializer
)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def create(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().select_related('author', 'group')
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def get_queryset(self):
        post = get_object_or_404(
            Post.objects.select_related('author', 'group'),
            pk=self.kwargs.get('post_id')
        )
        return post.comments.all()

    def perform_create(self, serializer):
        post = get_object_or_404(
            Post.objects.select_related('author', 'group'),
            pk=self.kwargs.get('post_id')
        )
        serializer.save(
            author=self.request.user,
            post=post
        )


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user__username', 'following__username')

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user.username)
        return user.follower

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

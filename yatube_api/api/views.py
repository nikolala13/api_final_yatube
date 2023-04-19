from django.shortcuts import get_object_or_404

from rest_framework import mixins, viewsets, filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly
)

from .permissions import AuthorOrReadOnly
from .serializers import (
    CommentSerializer,
    FollowSerializer,
    GroupSerializer,
    PostSerializer
)
from posts.models import Group, Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, AuthorOrReadOnly, )
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, AuthorOrReadOnly, )

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)
        self.post_id = get_object_or_404(Post, pk=self.kwargs.get('post_id'))

    def get_queryset(self):
        """Получаем queryset комментов к посту с нужным id."""
        new_queryset = self.post_id.comments.all()
        return new_queryset

    def perform_create(self, serializer):
        """Переопределяем сохранение автора и id поста."""
        serializer.save(author=self.request.user, post=self.post_id)


class FollowViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet
                    ):
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('=following__username', '=user__username',)

    def get_queryset(self):
        """Получаем queryset авторов, на кого подписан user."""
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

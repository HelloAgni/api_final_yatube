from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views

from api.views import PostViewSet, GroupViewSet
from api.views import CommentViewSet, FollowViewSet

router_v1 = routers.DefaultRouter()
router_v1.register('posts', PostViewSet)
router_v1.register('groups', GroupViewSet)
router_v1.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments')
router_v1.register('follow', FollowViewSet)

# api/v1/jwt   /create /refresh....

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    # path('v1/jwt/...')
]

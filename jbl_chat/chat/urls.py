from django.urls.conf import re_path
from . import views

urlpatterns = [
    re_path(r'^users/$', views.UserList.as_view(), name='users-list'),
    re_path(r'^chat/$', views.ChatList.as_view(), name='chat-get-list'),
    re_path(r'^chat/(?P<from_id>.+)&(?P<to_id>.+)/$', views.ChatList.as_view(), name='chat-list'),
]
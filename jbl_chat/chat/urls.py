from django.urls.conf import re_path
from . import views

urlpatterns = [
    re_path(r'^users/$', views.UserList.as_view(), name='users-list')
]
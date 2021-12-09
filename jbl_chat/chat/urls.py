from django.urls.conf import re_path
from . import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls import url

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="This is a simple chat webservice for Jobylon",
      contact=openapi.Contact(email="luiz.gustavo.silva1@outlook.com"),
      license=openapi.License(name="Jobylon License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'^users/$', views.UserList.as_view(), name='users-list'),
    re_path(r'^chat/$', views.ChatList.as_view(), name='chat-get-list'),
    re_path(r'^chat/(?P<from_id>.+)&(?P<to_id>.+)/$', views.ChatList.as_view(), name='chat-list'),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


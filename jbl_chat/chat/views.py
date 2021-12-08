from rest_framework import generics, serializers
from .models import User
from .serializers import UserSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):

        queryset = User.objects.all()
        return queryset

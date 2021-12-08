from rest_framework import generics, serializers
from .models import User, Chat
from .serializers import UserSerializer, ChatSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):

        queryset = User.objects.all()
        return queryset

class ChatList(generics.ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    def get_queryset(self):
        queryset = Chat.objects.all()
        from_id = self.request.query_params.get('from_id')
        to_id = self.request.query_params.get('to_id')

        if from_id is not None and to_id is not None:
            queryset = Chat.objects.filter(from_message=from_id or to_id,to_message=to_id or from_id)
        
        return queryset
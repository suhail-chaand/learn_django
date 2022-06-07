from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics, permissions

from django.contrib.auth.models import User
from snippets.serializers import UserSerializer

from snippets.permissions import IsOwnerOrReadOnly

# Create your views here.

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class SnippetDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class UserList(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class UserDetails(generics.RetrieveAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
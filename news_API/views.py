from rest_framework import generics

from .models import News
from .serializers import NewsSerializer
from .permissions import IsAuthorOrReadOnly

# Create your views here.
class NewsAPIView(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = News.objects.all()
    serializer_class = NewsSerializer

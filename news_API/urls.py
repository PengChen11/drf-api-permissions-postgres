from django.urls import path, include
from .views import NewsAPIView, NewsDetail

urlpatterns = [
    path('', NewsAPIView.as_view(), name='api'),
    path('<int:pk>/', NewsDetail.as_view(), name='details'),
]

from django.urls import path
from .views import (BookListAPIView,
                    BookDeleteAPIView,
                    BookDetailAPIView,
                    BookUpdateAPIView,
                    BookCreateAPIView,
                    BookViewSet
                    )

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('books', BookViewSet, basename="books")

urlpatterns = [
    #     path('books/', BookListAPIView.as_view()),
    #     path('book/<int:pk>/', BookDetailAPIView.as_view()),
    #     path('book/<int:pk>/update/', BookUpdateAPIView.as_view()),
    #     path('book/<int:pk>/delete/', BookDeleteAPIView.as_view()),
    #     path('book/create/', BookCreateAPIView.as_view()),
]

urlpatterns = urlpatterns + router.urls

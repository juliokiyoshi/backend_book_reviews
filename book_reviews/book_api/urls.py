from django.urls import path
from .views import BookRequests, BooksDetailRequest

urlpatterns = [
    path('', BookRequests.as_view()),
    path('<str:pk>', BooksDetailRequest.as_view())
]
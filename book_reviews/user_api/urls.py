from django.urls import path
from .views import UserRequests, UserDetailRequest

urlpatterns = [
    path('', UserRequests.as_view()),
    path('<str:pk>', UserDetailRequest.as_view())
]
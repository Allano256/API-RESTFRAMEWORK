from django.urls import path
from followers import views

urlpatterns = [
    path('folLower/',views.FollowerList.as_view()),
    path('follower/<int:pk>', views.FollowerList.as_view()),
]

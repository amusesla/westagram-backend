from django.urls import path

from .views import SignUpView, LoginView, FollowView

urlpatterns = [
    path('', SignUpView.as_view(), name='sign_up'),
    path('/login/', LoginView.as_view(), name='login'),
    path('/Follow/', FollowView.as_view(), name='follow'),
]

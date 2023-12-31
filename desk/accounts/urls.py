from django.urls import path
from .views import SignUp, show_profile
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('signup', SignUp.as_view(), name='signup'),
    path(r'logout/', LogoutView.as_view(), name='logout')
]

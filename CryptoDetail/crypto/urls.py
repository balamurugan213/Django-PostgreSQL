from django.urls import path
from .views import HomePageView
from .views import SignupPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('signup/', SignupPageView.as_view(), name='signup'),
]

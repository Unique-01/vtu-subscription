from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('signup/',views.SignUp.as_view(),name='signup'),
    path('login/',obtain_auth_token),
    path('logout/',views.LogoutView.as_view(),name='logout'),
]

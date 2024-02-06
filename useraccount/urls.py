from django.urls import path
from useraccount.views import UserLogin, signup_view, logout_request, UserLogin, signup_view, user_profile, update_profile

app_name = "user"

urlpatterns = [
    path('login/', UserLogin.as_view(), name="login"),
    path('register/', signup_view, name="register"),
    path("profile/", user_profile, name="profile"),
    path("update/<int:id>/", update_profile, name="update"),
    path('logout/', logout_request, name="logout"),
]
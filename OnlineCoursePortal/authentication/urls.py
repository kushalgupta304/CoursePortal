from .views import Signup, Login
from django.urls import path

urlpatterns = [
    path('signup/', Signup.as_view()),
        path('login/', Login.as_view()),

]

from rest_framework.routers import SimpleRouter
from .views import CourseViewSet, EnrollApiView, CourseAnalytics
from django.urls import path

router = SimpleRouter()

router.register('', CourseViewSet)

urlpatterns = [
    path('enroll', EnrollApiView.as_view()),
        path('analytics', CourseAnalytics.as_view()),

    
]
urlpatterns += router.urls

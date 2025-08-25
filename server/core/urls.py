from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, JobListingViewSet

router = DefaultRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'jobs', JobListingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
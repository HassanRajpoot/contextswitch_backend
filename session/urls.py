from rest_framework.routers import DefaultRouter
from .views import SessionViewSet

router = DefaultRouter()
router.register(r'sessions_set', SessionViewSet, basename='session_set')

urlpatterns = router.urls

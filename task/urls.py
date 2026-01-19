from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register(r'tasks_set', TaskViewSet, basename='task_set')

urlpatterns = router.urls
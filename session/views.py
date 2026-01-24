from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.utils.timezone import now
from django.db.models import Count
from .models import Session
from .serializers import SessionSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class SessionViewSet(ModelViewSet):
    serializer_class = SessionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Session.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=["get"])
    def insights(self, request):
        today = now().date()
        sessions = Session.objects.filter(
            user=request.user,
            start_time__date=today
        )

        data = {
            "total_sessions": sessions.count(),
            "switch_count": sessions.exclude(switch_reason=None).count(),
            "most_common_reason": sessions.values("switch_reason")
                .annotate(count=Count("switch_reason"))
                .order_by("-count")
                .first(),
        }

        return Response(data)
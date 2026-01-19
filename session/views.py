from rest_framework.viewsets import ModelViewSet
from .models import Session
from .serializers import SessionSerializer

class SessionViewSet(ModelViewSet):

    serializer_class = SessionSerializer

    def get_queryset(self):
        # Only return sessions belonging to logged-in user
        return Session.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically attach logged-in user
        serializer.save(user=self.request.user)
    
    def perform_update(self, serializer):
        # Automatically attach logged-in user
        serializer.save(user=self.request.user)
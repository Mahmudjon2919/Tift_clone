from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import ApplicationCreateSerializer, ApplicationDetailSerializer
from .models import Application
from rest_framework.permissions import IsAuthenticated


class ApplicationCreateAPIView(CreateAPIView):
    serializer_class = ApplicationCreateSerializer
    queryset = Application
    permission_classes = (IsAuthenticated,)


class ApplicationStatusesListAPIView(ListAPIView):
    serializer_class = ApplicationDetailSerializer
    queryset = Application.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)


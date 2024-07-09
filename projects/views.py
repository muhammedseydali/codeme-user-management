from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Project
from .serializers import ProjectSerializer
from rest_framework.parsers import MultiPartParser, FormParser


class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_parsers(self):
        if getattr(self, 'swagger_fake_view', False):
            return []
        return super().get_parsers()  

class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_parsers(self):
        if getattr(self, 'swagger_fake_view', False):
            return []
        return super().get_parsers()  
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from projects.permissions import IsManagerOrReadOnly, IsTeamLeadOrReadOnly, IsTeamMemberOrReadOnly
from rest_framework.parsers import MultiPartParser, FormParser


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsManagerOrReadOnly, IsTeamLeadOrReadOnly]

    def get_parsers(self):
        if getattr(self, 'swagger_fake_view', False):
            return []
        return super().get_parsers() 

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsManagerOrReadOnly, IsTeamLeadOrReadOnly, IsTeamMemberOrReadOnly]
    
    def get_parsers(self):
        if getattr(self, 'swagger_fake_view', False):
            return []
        return super().get_parsers() 

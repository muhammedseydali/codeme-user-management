from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdminOrReadOnly
from tasks.models import Task
from projects.models import Project
from projects.serializers import ProjectSerializer
from tasks.serializers import TaskSerializer
from rest_framework.parsers import MultiPartParser, FormParser


class AdminReportViews(APIView):
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    def get(self, request, format=None):
        projects = Project.objects.all()
        tasks = Task.objects.all()
        report_data = {
            'total_projects': projects.count(),
            'total_tasks': tasks.count(),
            'projects': ProjectSerializer(projects, many=True).data,
            'tasks': TaskSerializer(tasks, many=True).data
        }
        return Response(report_data)

    def get_parsers(self):
        if getattr(self, 'swagger_fake_view', False):
            return []
        return super().get_parsers()  

class ManagerReportViews(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        tasks = Task.objects.filter(project__assigned_to=request.user)
        report_data = {
            'total_tasks': tasks.count(),
            'tasks': TaskSerializer(tasks, many=True).data
        }
        return Response(report_data)

    def get_parsers(self):
        if getattr(self, 'swagger_fake_view', False):
            return []
        return super().get_parsers()  
    



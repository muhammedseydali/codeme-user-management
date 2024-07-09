from rest_framework import serializers
from .models import Project
from .models import CustomUser
# from rest_framework import serializers
# from .models import Project

# class ProjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Project
#         fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'created_at', 'updated_at', 'assigned_to']
from rest_framework import serializers
from .models import Category, Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'description', 'is_visible', 'weight')

class CategorySerializer(serializers.ModelSerializer):

    tasks = TaskSerializer(many=True)

    class Meta:
        model = Category
        fields = ('title', 'is_visible', 'tasks')

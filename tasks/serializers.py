from django.contrib.auth.models import User
from rest_framework import serializers
from tasks.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        read_only_fields = ('id','user','updated_at', 'created_at' )
        fields = ['id','user','title', 'description', 'updated_at', 'created_at']

    def to_representation(self, instance):
        """Convert `user` to its `username` (lowercased)."""
        ret = super().to_representation(instance)
        ret['user'] = instance.user.username
        return ret
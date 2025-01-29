from django.contrib.auth.models import User
from rest_framework import serializers
from tasks.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        read_only_fields = ('id','user','updated_at', 'created_at' )
        fields = ['id','user','title', 'description', 'updated_at', 'created_at']

    def create(self, validated_data):
        # Automatically set the user to the authenticated user
        user = self.context['request'].user  # Access the user from the request context
        return Task.objects.create(user=user, **validated_data)

    def to_representation(self, instance):
        """Convert `user` to its `username` (lowercased)."""
        ret = super().to_representation(instance)
        if instance.user:
            ret['user'] = instance.user.username
        return ret


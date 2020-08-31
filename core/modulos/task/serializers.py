from rest_framework import serializers

from core.models import Task

class TaskSerializer(serializers.HyperlinkedModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='task-highlight', format='html')

    class Meta:
        model = Task
        fields = '__all__'
    

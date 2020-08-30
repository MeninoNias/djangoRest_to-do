from django.contrib.auth.models import User
from rest_framework.serializers import HyperlinkedModelSerializer, HyperlinkedRelatedField

from ...models import Task

class UserSerializer(HyperlinkedModelSerializer):
    tasks = HyperlinkedRelatedField(many=True, view_name='task-detail', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'tasks']
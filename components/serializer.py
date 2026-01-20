from rest_framework import serializers
from projects.models import (
    Component
)

class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = "__all__"

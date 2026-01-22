from rest_framework import serializers
from components.serializer import ComponentSerializer
from projects.models import (
    Project,
    ComponentQuantityPerProject,
    Statusboard, 
    Story,
    UseCase
)


class ComponentQuantitySerializer(serializers.ModelSerializer):
    component = ComponentSerializer(read_only=True)
    class Meta:
        model = ComponentQuantityPerProject
        fields = ("component", "quantity")

        

class ProjectSerializer(serializers.ModelSerializer):
    components = ComponentQuantitySerializer(
        source="component_quantities",
        many=True,
        read_only=True
    )
    class Meta:
        model = Project
        fields = "__all__"

class StatusboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statusboard
        fields = "__all__"


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = "__all__"




class UsecaseboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = UseCase
        fields = "__all__"
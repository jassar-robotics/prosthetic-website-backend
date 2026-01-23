from rest_framework import serializers
from components.serializer import ComponentSerializer
from projects.models import (
    Project,
    ComponentQuantityPerProject,
    Statusboard, 
    Story,
    UseCase,
    Stage,
    StageImage,
    ProjectImage
)

# --- Sub-Serializers ---

class ComponentQuantitySerializer(serializers.ModelSerializer):
    # Pulls the full component details from ComponentSerializer
    component = ComponentSerializer(read_only=True)
    class Meta:
        model = ComponentQuantityPerProject
        fields = ("component", "quantity")

class StatusboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statusboard
        fields = "__all__"

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = "__all__"

class UseCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UseCase
        fields = "__all__"

class StageImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StageImage
        fields = ("id", "image")

class StageSerializer(serializers.ModelSerializer):
    # Matches related_name='stage_images' in StageImage model
    stage_images = StageImageSerializer(many=True, read_only=True)

    class Meta:
        model = Stage
        fields = ("id", "stage_no", "heading", "description", "image", "stage_images")

class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ("id", "image")


class ProjectSerializer(serializers.ModelSerializer):
    components = ComponentQuantitySerializer(
        source="component_quantities",
        many=True,
        read_only=True
    )
    stages = StageSerializer(many=True, read_only=True)
    stories = StorySerializer(many=True, read_only=True)
    use_cases = UseCaseSerializer(
        source="usecases",
        many=True, 
        read_only=True
    )
    status_updates = StatusboardSerializer(
        source="statusboard",
        many=True, 
        read_only=True
    )
    gallery = ProjectImageSerializer(
        source="project_images",
        many=True, 
        read_only=True
    )

    class Meta:
        model = Project
        fields = (
            "id", "name", "slug", "image", "which_hand", "status", "version", 
            "is_hidden", "description", "vision", "video_url", 
            "video_description_link", "circuit_diagram", "manuals",
            "software_github_link", "mechanical_github_repo_folder", 
            "electrical_github_repo", "software_github_repo",
            "readme_mechanical", "readme_electrical", "readme_software",
            "components", "stages", "stories", "use_cases", "status_updates", "gallery",
            "created_at", "modified_at"
        )
from django.contrib import admin

from core.mixins import DeleteLinkMixin
from projects.form import (ProjectAdminForm, StatusboardAdminForm, StoryAdminForm, UseCaseAdminForm, StageAdminForm)
from projects.models import (Project, Statusboard, Story, UseCase, Stage )





class StageInline(admin.TabularInline):
    model = Stage
    form = StageAdminForm
    extra = 1

    
class ProjectAdmin(DeleteLinkMixin, admin.ModelAdmin):
    form = ProjectAdminForm
    list_display = ("name", "status", "version", "is_hidden", "modified_at", "delete_link", )
    list_filter = ("status", "is_hidden", "which_hand")
    prepopulated_fields = {"slug": ("name",)}
    inlines = [StageInline]

 
    fieldsets = (
        ("Basic Info", {
            "fields": ("name", "slug", "image", "which_hand", "status", "version", "is_hidden"),
            "description": "Core identity and visibility settings for the project."
        }),
        ("Content & Media", {
            "fields": ("description", "vision", "video_url", "video_description_link"),
            "description": "Public-facing marketing and educational content."
        }),
        ("Technical Files", {
            "fields": ("circuit_diagram", "manuals"),
            "description": "Primary engineering assets for users."
        }),
        ("Contributor / Developer Resources", {
            "classes": ("collapse",),
            "fields": (
                "software_github_link", 
                "mechanical_github_repo_folder", 
                "electrical_github_repo", 
                "software_github_repo",
                "readme_mechanical",
                "readme_electrical",
                "readme_software"
            ),
            "description": "Deep-link resources for developers and engineers to contribute to the project."
        }),
    )


class StoryAdmin(DeleteLinkMixin, admin.ModelAdmin):
    form = StoryAdminForm
    list_display = ("name", "country", "is_accepted")
    list_filter = ("country", "is_accepted")
    search_fields = ("name", "story_content")
    filter_horizontal = ("projects",)

    fieldsets = (
        ("Basic Identification", {
            "fields": ("name", "country", "is_accepted")
        }),
        ("The Narrative", {
            "fields": ("story_content", "projects"),
        }),
    )


class UseCaseAdmin(admin.ModelAdmin):
    form = UseCaseAdminForm
    list_display = ("heading",)
    search_fields = ("heading", "description")
    filter_horizontal = ("projects",)

    fieldsets = (
        ("General Information", {
            "fields": ("heading", "description"),
        }),
        ("Associated Projects", {
            "fields": ("projects",),
            "description": "Select the projects that demonstrate this specific use case."
        }),
    )

class StatusboardAdmin(DeleteLinkMixin, admin.ModelAdmin):
    form = StatusboardAdminForm
    
    list_display = ("heading", "status", "modified_at")
    list_filter = ("status", "projects")
    search_fields = ("heading", "description")
    prepopulated_fields = {"slug": ("heading",)}
    filter_horizontal = ("projects",)

    fieldsets = (
        ("Header Info", {
            "fields": ("heading", "slug", "status"),
            "description": "Primary identification and current progress state."
        }),
        ("Details", {
            "fields": ("description", "projects"),
            "description": "Comprehensive task notes and project associations."
        }),
    )



class StageAdmin(admin.ModelAdmin):
    form = StageAdminForm
    list_display = ("project", "stage_no", "heading")
    list_filter = ("project",)
    search_fields = ("heading", "project__name")


admin.site.register(Story, StoryAdmin)
admin.site.register(Stage, StageAdmin)
admin.site.register(UseCase, UseCaseAdmin)
admin.site.register(Statusboard, StatusboardAdmin)
admin.site.register(Project, ProjectAdmin)
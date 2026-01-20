from django.contrib import admin

from core.mixins import DeleteLinkMixin
from projects.form import (ProjectAdminForm, StatusboardAdminForm)
from projects.models import (Project, Statusboard )


class ProjectNameMixin:
    def get_PROSTHETICS(self, obj):
        return obj.project.name if obj.project else "No Project Assigned"
    get_PROSTHETICS.short_description = "Project"





class StatusboardNameMixin:
    def get_statusboard_name(self, obj):
        return obj.statusboard.heading if obj.statusboard else "No Statusboard Assigned"
    get_statusboard_name.short_description = "Statusboard"





class ProjectAdmin(DeleteLinkMixin, admin.ModelAdmin):
    form = ProjectAdminForm
    list_display = ("name", "status", "version", "is_hidden", "modified_at", "delete_link", )
    list_filter = ("status", "is_hidden", "which_hand")
    prepopulated_fields = {"slug": ("name",)}

 
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


class StatusboardAdmin(StatusboardNameMixin, DeleteLinkMixin, admin.ModelAdmin):
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

admin.site.register(Statusboard, StatusboardAdmin)



admin.site.register(Project, ProjectAdmin)
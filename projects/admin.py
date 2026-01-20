from django.contrib import admin

from core.mixins import DeleteLinkMixin
from projects.form import (ProjectAdminForm)
from projects.models import (Project )


class ProjectNameMixin:
    def get_PROSTHETICS(self, obj):
        return obj.project.name if obj.project else "No Project Assigned"
    get_PROSTHETICS.short_description = "Project"



class ProjectAdmin(DeleteLinkMixin, admin.ModelAdmin):
    form = ProjectAdminForm
    list_display = ("name", "status", "version", "is_hidden", "modified_at", "delete_link", )
    list_filter = ("status", "is_hidden", "which_hand")
    prepopulated_fields = {"slug": ("name",)}

    fieldsets = (
        ("Basic Info", {
            "fields": ("name", "slug", "image", "which_hand", "status", "version", "is_hidden")
        }),
        ("Content & Media", {
            "fields": ("description", "vision", "video_url", "video_description_link", "stories")
        }),
        ("Technical Files", {
            "fields": ("circuit_diagram", "manuals")
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
            )
        }),
    )



    
admin.site.register(Project, ProjectAdmin)
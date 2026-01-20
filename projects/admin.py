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
    list_display = ("name", "modified_at", "delete_link", )
    prepopulated_fields = {"slug": ("name",)}

    fieldsets = (
        ("Basic Info", {
            "fields": (
                "name", "slug", "image", "description",
            )
        }),
    )


# ---------------- Register Models ----------------
admin.site.register(Project, ProjectAdmin)
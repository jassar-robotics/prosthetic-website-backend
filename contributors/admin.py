from django.contrib import admin

from core.mixins import DeleteLinkMixin
from contributors.form import (ContributorAdminForm)
from contributors.models import (Contributor)

class ContributorNameMixin:
    def get_contributor_name(self, obj):
        return obj.contributor.heading if obj.contributor else "No Contributor Assigned"
    get_contributor_name.short_description = "Contributor"



class ContributorAdmin(ContributorNameMixin, DeleteLinkMixin, admin.ModelAdmin):
    form = ContributorAdminForm
    
    list_display = ("name", "contributor_type", "email", "is_accepted", "is_hidden")
    list_filter = ("contributor_type", "is_accepted", "is_hidden")
    search_fields = ("name", "email", "phone")
    prepopulated_fields = {"slug": ("name",)}
    filter_horizontal = ("projects",)

    fieldsets = (
        ("Personal Information", {
            "fields": ("name", "slug", "image", "quote", "contributor_type"),
            "description": "Public profile details for the contributor."
        }),
        ("Contact & Status", {
            "fields": ("email", "phone", "is_accepted", "is_hidden"),
            "description": "Private contact info and administrative visibility controls."
        }),
        ("Contributions", {
            "fields": ("projects",),
            "description": "Linking the contributor to the projects they worked on."
        }),
        ("Submitted Files", {
            "classes": ("collapse",),
            "fields": ("file_mechanical", "file_electrical", "file_software", "file_others"),
            "description": "Technical files submitted by the contributor for review."
        }),
    )

admin.site.register(Contributor, ContributorAdmin)
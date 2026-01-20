from django.contrib import admin

from core.mixins import DeleteLinkMixin
from components.form import (ComponentAdminForm)
from components.models import (Component)

class ComponentNameMixin:
    def get_component_name(self, obj):
        return obj.component.heading if obj.component else "No Component Assigned"
    get_component_name.short_description = "Component"



class ComponentAdmin(ComponentNameMixin, DeleteLinkMixin, admin.ModelAdmin):
    form = ComponentAdminForm
    
    list_display = ("name", "type", "part_no", "version")
    list_filter = ("type",)
    search_fields = ("name", "part_no")
    prepopulated_fields = {"slug": ("name",)}

 
    fieldsets = (
        ("Identification", {
            "fields": ("name", "slug", "part_no", "version", "type"),
            "description": "Basic tracking information for the component inventory."
        }),
        ("Content & Specifications", {
            "fields": ("description", "specs", "image"),
            "description": "Visual and technical details used for the project documentation."
        }),
        ("External Resources & Files", {
            "fields": ("resource_url", "cad_file"),
            "description": "Links and downloadable assets for engineering and manufacturing."
        }),
    )

admin.site.register(Component, ComponentAdmin)
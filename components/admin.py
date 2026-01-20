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
    list_display = ("name",)
    prepopulated_fields = {"slug": ("name",)}


    fieldsets = (
        ("Basic Info", {
            "fields": (
                "name", "slug", "image",  "type", "description",
            )
        }),
    )

admin.site.register(Component, ComponentAdmin)
from django import forms
from tinymce.widgets import TinyMCE

from core.form import TINYMCE_BASIC_CONFIG
from components.models import (Component)


class ComponentAdminForm(forms.ModelForm):
    class Meta:
        model = Component
        fields = "__all__"
        widgets = {
            "content": TinyMCE(mce_attrs=TINYMCE_BASIC_CONFIG),
        }
        help_texts = {
            "name": "The full commercial or technical name of the component.",
            "slug": "Automatically generated from the name. Used for SEO-friendly URLs.",
            "part_no": "The unique manufacturer part number (MPN) or SKU.",
            "version": "Current iteration of the component (e.g., v1.0, Beta).",
            "type": "Categorize as Mechanical (hardware/frames) or Electrical (sensors/PCBs).",
            "description": "High-level overview of what this component does.",
            "specs": "Technical data sheet information, dimensions, and tolerances.",
            "image": "Clear photo or render of the component (Cloudinary processed).",
            "resource_url": "Link to external documentation, datasheet, or vendor page.",
            "cad_file": "Upload 3D models (STL, STEP, etc.) for mechanical integration.",
        }



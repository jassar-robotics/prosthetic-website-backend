from django import forms
from tinymce.widgets import TinyMCE

from core.form import TINYMCE_BASIC_CONFIG
from core.mixins import ImageSizeValidationMixin
from projects.models import ( Project, Statusboard)


class ProjectAdminForm(ImageSizeValidationMixin, forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"
        widgets = {
            "content": TinyMCE(mce_attrs=TINYMCE_BASIC_CONFIG),
        }
        help_texts = {
                "name": "The public-facing name of the project (e.g., 'Prosthetic Alpha').",
                "slug": "URL-friendly version of the name. Auto-generated.",
                "image": "Main display image. Processed via Cloudinary.",
                "which_hand": "Specify if this project is designed for the Left or Right hand.",
                "status": "Current lifecycle stage of the project.",
                "version": "Current release version (e.g., v2.1.0).",
                "is_hidden": "If checked, this project will not appear on the public website.",

                "description": "Main body text describing the project features and functionality.",
                "vision": "Long-term goals and the 'why' behind this specific design.",
                "video_url": "Main showcase video (e.g., YouTube or Vimeo link).",
                "video_description_link": "Link to a secondary video explaining technical details or assembly.",

                "circuit_diagram": "Upload the schematic file (preferably .sch format).",
                "manuals": "User guides or assembly instructions in PDF format.",

                "software_github_link": "Link to the primary software repository.",
                "mechanical_github_repo_folder": "Direct link to the CAD/Mechanical subfolder on GitHub.",
                "electrical_github_repo": "Link to the PCB/Electrical project files.",
                "software_github_repo": "Direct link to the source code repository for contributors.",
                "readme_mechanical": "Technical README PDF specifically for mechanical assembly.",
                "readme_electrical": "Technical README PDF for PCB fabrication and soldering.",
                "readme_software": "Technical README PDF for environment setup and flashing code.",
            }




class StatusboardAdminForm(forms.ModelForm):
    class Meta:
        model = Statusboard
        fields = "__all__"
        widgets = {
            "content": TinyMCE(mce_attrs=TINYMCE_BASIC_CONFIG),
        }
        help_texts = {
                    'projects': 'Select the project(s) this status board entry belongs to. Hold Ctrl/Cmd to select multiple.',
                    'heading': 'A brief, descriptive title for this status update (max 100 characters).',
                    'description': 'Provide detailed information about the progress or roadblocks (max 1000 characters).',
                    'status': 'Select the current workflow stage for this task.',
                    'slug': 'URL-friendly identifier generated from the heading. Used for direct linking.',
                }
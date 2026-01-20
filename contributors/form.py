from django import forms
from tinymce.widgets import TinyMCE

from core.form import TINYMCE_BASIC_CONFIG
from contributors.models import (Contributor)


class ContributorAdminForm(forms.ModelForm):
    class Meta:
        model = Contributor
        fields = "__all__"
        widgets = {
            "content": TinyMCE(mce_attrs=TINYMCE_BASIC_CONFIG),
        }
        help_texts = {
            'name': 'Enter the full legal or professional name of the contributor.',
            'quote': 'A short testimonial or biography that will appear on their profile.',
            'image': 'Upload a professional headshot. Recommended size: 500x500px.',
            'is_hidden': 'Hide this contributor from the public listing (useful for drafts).',
            'is_accepted': 'Check this once the contributor\'s identity and work have been verified.',
            'email': 'The main address used for project updates and notifications.',
            'phone': 'International format preferred (e.g., +1-555-010-999).',
            'contributor_type': 'The primary area of expertise for this contributor.',
            'projects': 'Hold down "Control" (or "Command" on Mac) to select more than one project.',
            'file_mechanical': 'Mechanical designs or assembly files (Format: .step, .stp).',
            'file_electrical': 'Electrical schematics or PCB layouts (Format: .sch).',
            'file_software': 'Source code files or scripts (Format: .py).',
            'file_others': 'Any additional documentation or PDFs (Format: .pdf, .docx).',
        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # Optional: You can also style the help text or inputs here
            self.fields['email'].widget.attrs.update({'placeholder': 'example@domain.com'})


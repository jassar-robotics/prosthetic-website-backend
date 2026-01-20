from django import forms
from tinymce.widgets import TinyMCE

from core.form import TINYMCE_BASIC_CONFIG
from core.mixins import ImageSizeValidationMixin
from projects.models import ( Project)


class ProjectAdminForm(ImageSizeValidationMixin, forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"
        widgets = {
            "content": TinyMCE(mce_attrs=TINYMCE_BASIC_CONFIG),
        }


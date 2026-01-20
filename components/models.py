from cloudinary.uploader import destroy, upload
from django.db import models
from tinymce.models import HTMLField

from django.core.validators import FileExtensionValidator

from core.choices import COMPONENT_TYPE_CHOICES
from core.mixins import (CloudinaryImageProcessingMixin)
from core.models import  BaseSlugModel
from components.manager import AllManager, NonHiddenManager, HiddenManager


class Component(BaseSlugModel, CloudinaryImageProcessingMixin):
    name = models.CharField(max_length=200, null=False, blank=False)
    type = models.CharField(choices=COMPONENT_TYPE_CHOICES, max_length=20)
    description = HTMLField()
    specs = HTMLField()
    cad_file = models.FileField(
        upload_to="cad_files/components/",
        null=True,
        blank=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=["stl", "step", "stp", "iges", "igs", "dwg", "dxf"]
            )
        ],
        help_text="Upload CAD files (STL, STEP, IGES, DWG, DXF)"
    )


    objects = AllManager()
    shown = NonHiddenManager()
    hidden = HiddenManager()

    class Meta:
        db_table = "components"

    def __str__(self):
        return f"{self.name}"
    
    def delete(self, *args, **kwargs):
        if self.image:
            destroy(self.image.public_id)
        super().delete(*args, **kwargs)

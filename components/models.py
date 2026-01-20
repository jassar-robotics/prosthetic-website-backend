from django.db import models
from tinymce.models import HTMLField

from django.core.validators import FileExtensionValidator

from core.choices import COMPONENT_TYPE_CHOICES
from core.mixins import HomeImageProcessingMixin
from core.models import  BaseSlugModel
from components.manager import AllManager, NonHiddenManager, HiddenManager


class Component(BaseSlugModel, HomeImageProcessingMixin):
    class ComponentType(models.TextChoices):
        MECHANICAL = 'MECHANICAL', 'Mechanical'
        ELECTRICAL = 'ELECTRICAL', 'Electrical'

    # Basic Fields
    name = models.CharField(max_length=100) # Updated to 100
    type = models.CharField(
        max_length=20, 
        choices=ComponentType.choices, 
        default=ComponentType.MECHANICAL
    )
    description = HTMLField()
    specs = HTMLField()

    # Media & Files
    image = models.ImageField(upload_to="components/images/", null=True, blank=True)
    resource_url = models.URLField(blank=True, null=True)
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

    # Versioning & Tracking
    version = models.CharField(max_length=20, blank=True)
    part_no = models.CharField(max_length=100, blank=True)

  


    objects = AllManager()
    shown = NonHiddenManager()
    hidden = HiddenManager()

    class Meta:
        db_table = "components"

    def __str__(self):
        return f"{self.name} ({self.part_no})" if self.part_no else self.name

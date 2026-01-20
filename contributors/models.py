from django.db import models
from django.core.validators import FileExtensionValidator

from core.mixins import HomeImageProcessingMixin
from core.models import  BaseSlugModel
from core.manager import AllManager, NonHiddenManager, HiddenManager


class Contributor(BaseSlugModel, HomeImageProcessingMixin):
    # Choice Definition
    class ContributorType(models.TextChoices):
        ELECTRIC = 'ELECTRIC', 'Electric'
        MECHANIC = 'MECHANIC', 'Mechanic'
        SOFTWARE = 'SOFTWARE', 'Software'
        OTHERS = 'OTHERS', 'Others'

    # Identity & Status
    name = models.CharField(
        max_length=50, 
    )
    quote = models.TextField(
        blank=True, 
    )
    image = models.ImageField(
        upload_to="contributors/images/", 
        null=True, 
        blank=True,
    )
    is_hidden = models.BooleanField(
        default=False, 
    )
    is_accepted = models.BooleanField(
        default=False, 
    )

    # Contact & Role
    email = models.EmailField()
    phone = models.CharField(
        max_length=25, 
        blank=True, 
    )
    contributor_type = models.CharField(
        max_length=20, 
        choices=ContributorType.choices, 
        default=ContributorType.OTHERS,
    )

    # Relationship
    projects = models.ManyToManyField(
        'projects.Project', 
        blank=True,
    )

    # File Submissions
    file_mechanical = models.FileField(
        upload_to="contributors/files/mechanical/",
        null=True, blank=True,
        validators=[FileExtensionValidator(allowed_extensions=["step", "stp"])],
    )
    file_electrical = models.FileField(
        upload_to="contributors/files/electrical/",
        null=True, blank=True,
        validators=[FileExtensionValidator(allowed_extensions=["sch"])],
        
    )
    file_software = models.FileField(
        upload_to="contributors/files/software/",
        null=True, blank=True,
        validators=[FileExtensionValidator(allowed_extensions=["py", "zip"])],
    )
    file_others = models.FileField(
        upload_to="contributors/files/others/",
        null=True, blank=True,
        validators=[FileExtensionValidator(allowed_extensions=["doc", "docx", "pdf"])],
    )

    objects = AllManager()
    shown = NonHiddenManager()
    hidden = HiddenManager()

    class Meta:
        db_table = "contributors"

    def __str__(self):
        return f"{self.name} ({self.contributor_type})"
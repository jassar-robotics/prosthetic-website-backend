from cloudinary.uploader import destroy, upload
from django.db import models
from tinymce.models import HTMLField


from core.mixins import (CloudinaryImageProcessingMixin)
from core.models import  BaseSlugModel
from projects.manager import AllManager, NonHiddenManager, HiddenManager
from components.models import Component






class Project(BaseSlugModel, CloudinaryImageProcessingMixin):
    # Choice Definitions
    class HandChoices(models.TextChoices):
        LEFT = 'LEFT', 'Left'
        RIGHT = 'RIGHT', 'Right'

    class StatusChoices(models.TextChoices):
        UPCOMING = 'UPCOMING', 'Upcoming'
        ONGOING = 'ONGOING', 'Ongoing'
        FINAL = 'FINAL', 'Final'

    # Basic Info
    name = models.CharField(max_length=50) # Updated to 50 as requested
    image = models.ImageField(upload_to='projects/images/', blank=True, null=True)
    which_hand = models.CharField(max_length=10, choices=HandChoices.choices, default=HandChoices.RIGHT)
    circuit_diagram = models.FileField(upload_to='projects/circuits/', blank=True, null=True) # .sch
    manuals = models.FileField(upload_to='projects/manuals/', blank=True, null=True) # .pdf
    video_url = models.URLField(blank=True, null=True)

    # Meta & Description
    software_github_link = models.URLField(blank=True, null=True)
    video_description_link = models.URLField(blank=True, null=True)
    status = models.CharField(max_length=15, choices=StatusChoices.choices, default=StatusChoices.UPCOMING)
    version = models.CharField(max_length=20, blank=True)
    description = HTMLField()

    # Relations & Visibility
    stories = models.ManyToManyField('Stories', blank=True)
    is_hidden = models.BooleanField(default=False)

    # Contributor URLs
    mechanical_github_repo_folder = models.URLField(blank=True, null=True)
    electrical_github_repo = models.URLField(blank=True, null=True)
    software_github_repo = models.URLField(blank=True, null=True)
    vision = HTMLField(blank=True, null=True)

    # Contributor Files
    readme_mechanical = models.FileField(upload_to='projects/readmes/', blank=True, null=True)
    readme_electrical = models.FileField(upload_to='projects/readmes/', blank=True, null=True)
    readme_software = models.FileField(upload_to='projects/readmes/', blank=True, null=True)

    # Existing components and managers
    components = models.ManyToManyField(
        "Component",
        through="ComponentQuantityPerProject",
        related_name="projects",
        blank=True
    )
    objects = AllManager()
    shown = NonHiddenManager()
    hidden = HiddenManager()
    
    class Meta:
        db_table = "projects"

    def __str__(self):
        return f"{self.id}: {self.name}"

    def delete(self, *args, **kwargs):
        if self.image:
            try:
                destroy(self.image.public_id)
            except:
                pass 
        super().delete(*args, **kwargs)






        

class ComponentQuantityPerProject(models.Model):
    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        related_name="component_quantities"
    )
    component = models.ForeignKey(
        "components.Component",
        on_delete=models.CASCADE,
        related_name="project_quantities"
    )
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = "component_quantity_per_project"
        unique_together = ("project", "component")
        verbose_name = "Component Quantity per Project"
        verbose_name_plural = "Component Quantities per Project"

    def __str__(self):
        return f"{self.project.name} - {self.component.name} (x{self.quantity})"
    
    




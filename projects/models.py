from cloudinary.uploader import destroy, upload
from django.db import models
from tinymce.models import HTMLField


from core.mixins import (CloudinaryImageProcessingMixin)
from core.models import  BaseSlugModel
from projects.manager import AllManager, NonHiddenManager, HiddenManager
from components.models import Component




class Project(BaseSlugModel, CloudinaryImageProcessingMixin):
    name = models.CharField(max_length=200)
    description = HTMLField()


    components = models.ManyToManyField(
        Component,
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
            destroy(self.image.public_id)
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
    
    



